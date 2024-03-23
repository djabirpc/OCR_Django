import pytesseract
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ImageUploadSerializer
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

class OCRAPIView(APIView):
    def post(self, request, format=None):
        serializer = ImageUploadSerializer(data=request.data)
        if serializer.is_valid():
            image = serializer.validated_data['image']
            image = Image.open(image)
            ocr_result = pytesseract.image_to_string(image)
            try:
                ocr_result = pytesseract.image_to_string(image)
                return Response({'ocr_result': ocr_result}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)