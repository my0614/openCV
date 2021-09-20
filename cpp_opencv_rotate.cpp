
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <iostream>

using namespace cv;
using namespace std;


int main()
{
	Mat src = imread("./sample.png");           //reading image file in mat object
	double offsetX, offsetY;
	double angle = 45;
	double width = src.size().width;
	double height = src.size().height;

	Point2d center = Point2d(width / 2, height / 2);
	Rect bounds = RotatedRect(center, src.size(), angle).boundingRect();
	Mat result = Mat::zeros(bounds.size(),src.type());
	offsetX = (bounds.width - width) / 2;
	offsetY = (bounds.height - height) / 2;
	Rect roi = Rect(offsetX, offsetY, width, height);
	src.copyTo(result(roi));
	center += Point2d(offsetX, offsetY);
	Mat M = getRotationMatrix2D(center, angle, 1.0);
	warpAffine(result, result, M, result.size());
	imshow("result", result);         //displaying output image file
	waitKey(0);                     //to exit press escape
	return 0;
}
