#pragma once

#ifdef __cplusplus
extern "C" {
#endif

int InitEngine(char* szLicensePath);
int GetLiveness(unsigned char* pbBgrData, int width, int height, int* faceBox);
int ProcessAll(unsigned char* pbBgrData, int width, int height, int* faceBox, int* attribute,
    double* angles, int* liveness, int* age, int* gender, int* mask, unsigned char* pbFeature, int* featureSize, int mode);
double CompareFace(unsigned char* pbFeature1, int featureSize1, unsigned char* pbFeature2, int featureSize2);

#ifdef __cplusplus
}
#endif