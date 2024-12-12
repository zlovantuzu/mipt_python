"""
Шаблонный метод (Template method)
"""
import cv2
import numpy
import random


def image_hu_moments(func):
    def wrapper(*args, **kwargs):
        canny_output = func(*args, **kwargs)

        contours, _ = cv2.findContours(canny_output, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        mu = [None] * len(contours)
        for i in range(len(contours)):
            mu[i] = cv2.moments(contours[i])
        # Get the mass centers
        mc = [None] * len(contours)
        for i in range(len(contours)):
            # add 1e-5 to avoid division by zero
            mc[i] = (mu[i]['m10'] / (mu[i]['m00'] + 1e-5), mu[i]['m01'] / (mu[i]['m00'] + 1e-5))

        drawing = numpy.zeros((canny_output.shape[0], canny_output.shape[1], 3), dtype=numpy.uint8)

        for i in range(len(contours)):
            color = (random.randint(0, 256), random.randint(0, 256), random.randint(0, 256))
            cv2.drawContours(drawing, contours, i, color, 2)
            cv2.circle(drawing, (int(mc[i][0]), int(mc[i][1])), 4, color, -1)

        for i in range(len(contours)):
            print(' * Contour[%d] - Area (M_00) = %.2f - Area OpenCV: %.2f - Length: %.2f' % (i, mu[i]['m00'], cv2.contourArea(contours[i]), cv2.arcLength(contours[i], True)))

        return canny_output, mu, mc
    return wrapper


class ObjectAnalysis(object):
    def template_method(self, image):
        image = self.noise_filtering(image)
        data = self.segmentation(image)
        data = self.object_parameters(data)

        return data

    def noise_filtering(self, image):
        raise NotImplementedError()

    def segmentation(self, data):
        raise NotImplementedError()

    def object_parameters(self, data):
        (image, data) = data
        (numLabels, labels, stats, centroids) = data
        x = []
        y = []
        w = []
        h = []
        area = []
        for i in range(1, numLabels):
            # extract the connected component statistics for the current
            # label
            x.append(stats[i, cv2.CC_STAT_LEFT])
            y.append(stats[i, cv2.CC_STAT_TOP])
            w.append(stats[i, cv2.CC_STAT_WIDTH])
            h.append(stats[i, cv2.CC_STAT_HEIGHT])
            area.append(stats[i, cv2.CC_STAT_AREA])

        return x, y, w, h, area


class BinaryImage(ObjectAnalysis):
    def __init__(self):
        pass

    def noise_filtering(self, image):
        median = cv2.medianBlur(image, 5)
        return median

    def segmentation(self, image):
        output = cv2.connectedComponentsWithStats(
            image,
            4,  # connectivity
            cv2.CV_32S)
        return image, output



class MonochromeImage(BinaryImage):
    def __init__(self):
        pass

    def noise_filtering(self, image):
        dst = cv2.GaussianBlur(image, (5, 5), 0)
        return dst

    def segmentation(self, image):
        output = cv2.Canny(image, 100, 200)
        return image, output


class ColorImage(MonochromeImage):
    def __init__(self):
        pass

    @image_hu_moments
    def canny(self, image):
        return cv2.Canny(image, 100, 200)

    def noise_filtering(self, image):
        b, g, r = cv2.split(image)
        blur_b = cv2.GaussianBlur(b, (3, 3), 0)
        blur_g = cv2.GaussianBlur(g, (3, 3), 0)
        blur_r = cv2.GaussianBlur(r, (3, 3), 0)
        blur_img = cv2.merge([blur_b, blur_g, blur_r])
        return blur_img

    def segmentation(self, image):
        image[numpy.all(image == 255, axis=2)] = 0

        kernel = numpy.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]], dtype=numpy.float32)
        imgLaplacian = cv2.filter2D(image, cv2.CV_32F, kernel)
        sharp = numpy.float32(image)
        imgResult = sharp - imgLaplacian

        # convert back to 8bits gray scale
        imgResult = numpy.clip(imgResult, 0, 255)
        imgResult = imgResult.astype('uint8')

        bw = cv2.cvtColor(imgResult, cv2.COLOR_BGR2GRAY)
        _, bw = cv2.threshold(bw, 40, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        dist = cv2.distanceTransform(bw, cv2.DIST_L2, 3)

        cv2.normalize(dist, dist, 0, 1.0, cv2.NORM_MINMAX)

        markers = numpy.zeros_like(bw, dtype=numpy.int32)
        markers[bw == 255] = 1
        markers[bw == 0] = 2

        _, dist = cv2.threshold(dist, 0.4, 1.0, cv2.THRESH_BINARY)
        kernel1 = numpy.ones((3, 3), dtype=numpy.uint8)
        dist = cv2.dilate(dist, kernel1)

        dist_8u = dist.astype('uint8')
        contours, _ = cv2.findContours(dist_8u, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        markers = numpy.zeros(dist.shape, dtype=numpy.int32)
        for i in range(len(contours)):
            cv2.drawContours(markers, contours, i, (i + 1), -1)
        cv2.circle(markers, (5, 5), 3, (255, 255, 255), -1)

        cv2.watershed(imgResult, markers)

        colors = []
        for contour in contours:
            colors.append((random.randint(0, 256), random.randint(0, 256), random.randint(0, 256)))

        dst = numpy.zeros((markers.shape[0], markers.shape[1], 3), dtype=numpy.uint8)

        for i in range(markers.shape[0]):
            for j in range(markers.shape[1]):
                index = markers[i, j]
                if 0 < index <= len(contours):
                    dst[i, j, :] = colors[index - 1]

        return image, dst


"""
Декоратор - структурный паттерн
"""


class FilteredAnalysis(ObjectAnalysis):
    def __init__(self, obj):
        self._proc = obj

    def template_method(self, image):
        (_x, _y, _w, _h, _area) = self._proc.template_method(image)
        x = []
        y = []
        w = []
        h = []
        area = []

        for i in range(len(_area)):
            if 10 < _area[i] < 2500:
                x.append(_x[i])
                y.append(_y[i])
                w.append(_w[i])
                h.append(_h[i])
                area.append(_area[i])

        return x, y, w, h, area


if __name__ == '__main__':
    # print("Binary Image Processing")
    # bin_segm = BinaryImage()
    # (x, y, w, h, area) = bin_segm.template_method(cv2.imread('./data/1.jpg', cv2.IMREAD_GRAYSCALE))
    # for i in range(len(area)):
    #     print([x[i], y[i], w[i], h[i], area[i]])

    # print("Decorated Binary Image Processing")
    # filt_bin = FilteredAnalysis(BinaryImage())
    # (x, y, w, h, area) = filt_bin.template_method(cv2.imread('./data/1.jpg', cv2.IMREAD_GRAYSCALE))
    # for i in range(len(area)):
    #     print([x[i], y[i], w[i], h[i], area[i]])

    print("Color Image segmentation")
    color_segm = ColorImage()
    img = cv2.imread('../data/cards.png')
    _, output = color_segm.segmentation(img)
    cv2.imwrite("../data/cards_s_res.png", output)


    print("Color Image noise_filtering")
    img = cv2.imread('../data/cards.png')
    output = color_segm.noise_filtering(img)
    cv2.imwrite("../data/cards_f_res.png", output)

    print("Color Image canny and image_hu_moments")
    img = cv2.imread('../data/cards.png')
    contours, mu, mc = color_segm.canny(img)

    f = open("../data/mu.txt", 'w')
    for elem in mu:
        print(elem, file=f)
    f.close()

    f = open("../data/mc.txt", 'w')
    for elem in mc:
        print(elem, file=f)
    f.close()

    cv2.imwrite("../data/cards_hu_res.png", contours)


