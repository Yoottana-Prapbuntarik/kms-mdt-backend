from rest_framework import status, mixins
from rest_framework import generics, permissions
from knox.models import AuthToken
from knox.auth import TokenAuthentication
from rest_framework.response import Response 
from .serializer import CreateDocumentReviewSerializer, DocumentTypeSerializer, DocumentTemplateSerializer
from .models import DocumentReview, DocumentType, DocumentTemplate

class CreateDocumentReviewApi(generics.CreateAPIView):
    """Create Agreement Content View """
    authentication_classes = (TokenAuthentication,)
    permission_classes = [ permissions.IsAuthenticated,]
    serializer_class = CreateDocumentReviewSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
                # document_type = number,
                # user = number,
                # student_name = string,
                # student_code = string,
                # document_status = approve , reject, waiting
                # document_file_review = mdt,mda,mmdt
            document_type = serializer.validated_data.get('document_type')
            student_name = serializer.validated_data.get('student_name')
            student_code = serializer.validated_data.get('student_code')
            document_status = serializer.validated_data.get('document_status')
            document_file_review = serializer.validated_data.get('document_file_review')
            serializer.save(document_type=document_type, user=self.request.user, student_name=student_name, student_code=student_code, document_status=document_status, document_file_review=document_file_review)
            return Response({'key_message': 'Created Document successfully' , 'status': status.HTTP_200_OK})

        return Response({'key_message': 'Cannot Create'}, status=status.HTTP_400_BAD_REQUEST)

class DocumentCategoryApi(generics.ListAPIView):
    queryset = DocumentType.objects.all()
    serializer_class = DocumentTypeSerializer
    def get_queryset(self):
        data = self.queryset.all()
        return data

class DocumentTemplateApi(generics.ListAPIView):
    queryset = DocumentTemplate.objects.all()
    serializer_class = DocumentTemplateSerializer
    def get_queryset(self):
        data = self.queryset.all()
        return data

class GetDocumentAPI(generics.ListAPIView):

  serializer_class = DocumentTemplateSerializer
  def get_queryset(self):
      queryset = DocumentTemplate.objects.filter(department=self.kwargs['department'])
      return queryset

class GetDocumentAPIById(generics.ListAPIView):

  serializer_class = DocumentTemplateSerializer
  def get_queryset(self):
      print(self.kwargs['id'])
      queryset = DocumentTemplate.objects.filter(id=self.kwargs['id'])
      return queryset

class GetDocumentReviewAPI(generics.ListAPIView):

  serializer_class = CreateDocumentReviewSerializer
  def get_queryset(self):
      queryset = DocumentReview.objects.all()
      return queryset


class DocumentUpdate(generics.RetrieveUpdateAPIView, mixins.UpdateModelMixin):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = DocumentReview.objects.all()
    serializer_class = CreateDocumentReviewSerializer
    def put(self, request, *args, **kwargs):
        data = self.queryset.filter(user=self.request.user).filter(id=self.kwargs['pk'])
        print(data)
        if(len(data) == 0):
            return Response({'key_message': 'Can not updated this is not document your own.'}, status=status.HTTP_400_BAD_REQUEST)
        else:    
            return self.update(request, *args, **kwargs)

class DeleteDocument(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = DocumentReview.objects.all()
    serializer_class = CreateDocumentReviewSerializer
    def delete(self, request, *args, **kwargs):
        data_for_delete = self.queryset.filter(user=self.request.user).filter(id=self.kwargs['pk'])
        print(data_for_delete)
        if(len(data_for_delete) == 0):
            return Response({'key_message': 'Can not Delete this is not document your own.'}, status=status.HTTP_400_BAD_REQUEST)
        else:    
            data_for_delete.delete()
            return Response({'key_message': 'Deleted  document successully.'}, status=status.HTTP_204_NO_CONTENT)
