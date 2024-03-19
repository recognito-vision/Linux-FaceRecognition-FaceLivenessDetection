
#include <stdio.h>
#include <string>
#include <vector>
#include <string>
#include <stdlib.h>
#include <time.h>
#include <sys/time.h>
#include <dirent.h>
#include <unistd.h>
#include <opencv2/opencv.hpp>

#include "faceengine.h"

using namespace std;

int main(int argc, char* argv[])
{
    int ret = InitEngine("../../license.txt");
    printf("init ret: %d\n", ret);

    int faceBox[4] = { 0 };
    int attribute[4] = { 0 };
    int liveness = 0, age = 0, gender = 0, mask = 0;
    double faceAngles[3] = { 0 };
    unsigned char feature[4096] = { 0 };
    int featureLen = 0;
    unsigned char feature1[4096] = { 0 };
    int featureLen1 = 0;

    cv::Mat image = cv::imread("../../examples/1.jpg");
    ProcessAll(image.data, image.cols, image.rows, faceBox, attribute, faceAngles, &liveness, &age, &gender, &mask, feature, &featureLen, 0);//register

    cv::Mat image1 = cv::imread("../../examples/2.jpg");
    ProcessAll(image1.data, image1.cols, image1.rows, faceBox, attribute, faceAngles, &liveness, &age, &gender, &mask, feature1, &featureLen1, 1);//verify

    double similarity = CompareFace(feature, featureLen, feature1, featureLen1);
    printf("matching score 1.jpg-2.jpg: %f\n", similarity);

    cv::Mat image2 = cv::imread("../../examples/5.jpg");
    ProcessAll(image2.data, image2.cols, image2.rows, faceBox, attribute, faceAngles, &liveness, &age, &gender, &mask, feature1, &featureLen1, 1);//verify
    similarity = CompareFace(feature, featureLen, feature1, featureLen1);
    printf("matching score 1.jpg-5.jpg: %f\n", similarity);
    return 0;
}