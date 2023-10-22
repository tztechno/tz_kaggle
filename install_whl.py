These whl files were collected by downloading under internet-on environment.

!pip download pylibjpeg
!pip download pylibjpeg-openjpeg
!pip download pylibjpeg-libjpeg 
!pip download pydicom 
!pip download python-gdcm
!pip download dicomsdl
  
Under inernet-off environment, use the following scripts to install them.

!pip install pylibjpeg --no-index --find-links=file:///kaggle/input/read-dicom-set
!pip install pylibjpeg-openjpeg --no-index --find-links=file:///kaggle/input/read-dicom-set
!pip install pylibjpeg-libjpeg --no-index --find-links=file:///kaggle/input/read-dicom-set
!pip install pydicom --no-index --find-links=file:///kaggle/input/read-dicom-set
!pip install python-gdcm --no-index --find-links=file:///kaggle/input/read-dicom-set
!pip install dicomsdl --no-index --find-links=file:///kaggle/input/read-dicom-set
