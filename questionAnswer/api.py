from rest_framework import status
from rest_framework import generics, permissions
from knox.models import AuthToken
from knox.auth import TokenAuthentication
from rest_framework.response import Response 
from .serializer import QuestionTopicSerializer, QuestionTopicViewSerializer, GetCommentQuestionCommentSerializers, CommentQuestionCommentSerializers
from .models import QuestionTopic, CommentQuestion

class PostQuestionAPI(generics.CreateAPIView):
    """Create Agreement Content View """
    authentication_classes = (TokenAuthentication,)
    permission_classes = [ permissions.IsAuthenticated,]
    serializer_class = QuestionTopicSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            sub_title = serializer.validated_data.get('sub_title')
            question_detail = serializer.validated_data.get('question_detail')
            question_image = serializer.validated_data.get('question_image')
            category = serializer.validated_data.get('category')

            serializer.save(title = title, sub_title=sub_title, question_detail=question_detail, question_image=question_image, category=category, own_user=self.request.user)
            return Response({'key_message': 'Created Question successfully' , 'status': status.HTTP_200_OK})

        return Response({'key_message': 'Cannot Create'}, status=status.HTTP_400_BAD_REQUEST)


class QuestionContentViewAllAPI(generics.ListAPIView):

    queryset = QuestionTopic.objects.all()
    serializer_class = QuestionTopicViewSerializer
    def get_queryset(self):
        """Return objects fot the current authenticated user only"""
        
        data = self.queryset.all()
        return data

    def list(self, request):
        queryset_list = self.get_queryset().all()
        serializer_list = QuestionTopicViewSerializer(queryset_list, many=True)
        data = {'question': serializer_list.data}
        return Response(data)


class GetCommentQuestionViewAPI(generics.ListAPIView):

    serializer_class = GetCommentQuestionCommentSerializers
    def get_queryset(self):
        queryset = CommentQuestion.objects.filter(question__id=self.kwargs['pk'])
        return queryset



class QuestionCommentAPI(generics.CreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = [ permissions.IsAuthenticated,]
    serializer_class = CommentQuestionCommentSerializers
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            question = serializer.validated_data.get('question')
            user_comment = serializer.validated_data.get('user_comment') 
            content = serializer.validated_data.get('content')
            
            serializer.save(question=question, user_comment=user_comment, content=content)
            return Response({'key_message': 'Comment question successfully'})
        return Response({'key_message': "Can not comment"}, status=status.HTTP_400_BAD_REQUEST)