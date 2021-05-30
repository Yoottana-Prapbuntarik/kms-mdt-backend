
from django.db.models import query
from rest_framework import status, mixins, generics, permissions
from knox.models import AuthToken
from .models import Blog, BlogCategory, Comment, ArticleLikeAndUnlike
from knox.auth import TokenAuthentication
from rest_framework.response import Response
from .serializer import BlogSerialzer, BlogContentViewSerializer, GetBlogCommentSerializers, BlogCategorySerializer,BlogCommentSerializers, ArticleLikeAndUnlikeSerializer, BlogDeleteSerialzer, UpdateBlogCommentSerializers, SearchBlogSerialzer
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

class BlogAPI(generics.CreateAPIView):
    """Create Agreement Content View """
    authentication_classes = (TokenAuthentication,)
    permission_classes = [ permissions.IsAuthenticated,]
    serializer_class = BlogSerialzer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            content = serializer.validated_data.get('content')
            title = serializer.validated_data.get('title')
            sub_title = serializer.validated_data.get('sub_title')
            cover = serializer.validated_data.get('cover')
            category = serializer.validated_data.get('category')

            serializer.save(content=content, own_user=self.request.user, title = title, sub_title=sub_title,category=category, cover=cover)
            return Response({'key_message': 'Created blog successfully' , 'status': status.HTTP_200_OK})

        return Response({'key_message': 'Cannot Create'}, status=status.HTTP_400_BAD_REQUEST)
    
class GetBlogCommentViewAPI(generics.ListAPIView):

    serializer_class = GetBlogCommentSerializers
    def get_queryset(self):
        queryset = Comment.objects.filter(article__id=self.kwargs['pk'])
        return queryset

class BlogCommentAPI(generics.CreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = [ permissions.IsAuthenticated,]
    serializer_class = BlogCommentSerializers
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            article = serializer.validated_data.get('article')
            user_comment = serializer.validated_data.get('user_comment') 
            content = serializer.validated_data.get('content')
            
            serializer.save(article=article, user_comment=user_comment, content=content)
            return Response({'key_message': 'Comment blog successfully'})
        return Response({'key_message': "Can not comment"}, status=status.HTTP_400_BAD_REQUEST)
        
class BlogContentViewAPI(generics.ListAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = [permissions.IsAuthenticated,]
    serializer_class = BlogContentViewSerializer
    queryset = Blog.objects.all()

    def get_queryset(self):
        """Return objects fot the current authenticated user only"""
        data = self.queryset.filter(own_user=self.request.user)
        return data

    def list(self, request):
        queryset_list = self.get_queryset().order_by('-id')
        serializer_list = BlogContentViewSerializer(queryset_list, many=True)
        data = {'blog': serializer_list.data}
        return Response(data)


class BlogDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogContentViewSerializer

class BlogContentViewAllAPI(generics.ListAPIView):

    queryset = Blog.objects.all()
    serializer_class = BlogContentViewSerializer
    def get_queryset(self):
        """Return objects fot the current authenticated user only"""
        
        data = self.queryset.all()
        return data

    def list(self, request):
        queryset_list = self.get_queryset().order_by('-pub_date').filter(published=True)
        serializer_list = BlogContentViewSerializer(queryset_list, many=True)
        data = {'blog': serializer_list.data}
        return Response(data)

class BlogCategoryAPI(generics.ListAPIView):
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategorySerializer
    def get_queryset(self):
        data = self.queryset.all()
        return data
    
    def list(self, request):
        queryset_list = self.get_queryset().order_by('-id')
        serializer_list = BlogCategorySerializer(queryset_list, many=True)
        data = {'category': serializer_list.data}
        return Response(data)



class BlogByCategoryItem(generics.ListAPIView):
    serializer_class = BlogContentViewSerializer
    def get_queryset(self):
        return Blog.objects.filter(category=self.kwargs.get('category_name',None))


# Remove and update

class BlogUpdate(generics.RetrieveUpdateAPIView, mixins.UpdateModelMixin):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Blog.objects.all()
    serializer_class = BlogSerialzer
    def put(self, request, *args, **kwargs):
        data = self.queryset.filter(own_user=self.request.user).filter(id=self.kwargs['pk'])
        print(data)
        if(len(data) == 0):
            return Response({'key_message': 'Can not updated this is not your own.'}, status=status.HTTP_400_BAD_REQUEST)
        else:    
            return self.update(request, *args, **kwargs)


class DeleteBlog(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Blog.objects.all()
    serializer_class = BlogDeleteSerialzer
    def delete(self, request, *args, **kwargs):
        # find for check is user ? and check id
        data_for_delete = self.queryset.filter(own_user=self.request.user).filter(id=self.kwargs['pk'])
        print(data_for_delete)
        if(len(data_for_delete) == 0):
            return Response({'key_message': 'Can not Delete this is not document your own.'}, status=status.HTTP_400_BAD_REQUEST)
        else:    
            data_for_delete.delete()
            return Response({'key_message': 'Deleted  document successully.'}, status=status.HTTP_204_NO_CONTENT)

#  Update comment

class GetBlogCommentViewByIdAPI(generics.ListAPIView):

    serializer_class = GetBlogCommentSerializers
    def get_queryset(self):
        queryset = Comment.objects.filter(user_comment__id=self.kwargs['pk'])
        return queryset

class UpdateComment(generics.RetrieveUpdateAPIView, mixins.UpdateModelMixin):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Comment.objects.all()
    serializer_class = UpdateBlogCommentSerializers
    def put(self, request, *args, **kwargs):
        print(self.kwargs['pk'])
        data = self.queryset.filter(id=self.kwargs['pk'])
        data = self.queryset.filter(user_comment=self.request.user).filter(id=self.kwargs['pk'])
        print(data)
        if(len(data) == 0):
            return Response({'key_message': 'Can not updated this is not your own.'}, status=status.HTTP_400_BAD_REQUEST)
        else:    
            return self.update(request, *args, **kwargs)


class DeleteComment(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Comment.objects.all()
    serializer_class = GetBlogCommentSerializers
    def delete(self, request, *args, **kwargs):
        # find for check is user ? and check id
        data_for_delete = self.queryset.filter(user_comment=self.request.user).filter(id=self.kwargs['pk'])
        print(data_for_delete)
        if(len(data_for_delete) == 0):
            return Response({'key_message': 'Can not Delete this is not comment your own.'}, status=status.HTTP_400_BAD_REQUEST)
        else:    
            data_for_delete.delete()
            return Response({'key_message': 'Deleted  comment successully.'}, status=status.HTTP_204_NO_CONTENT)


class LikeAndUnlikeApi(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = ArticleLikeAndUnlike.objects.all()
    serializer_class = ArticleLikeAndUnlikeSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user_like = serializer.validated_data.get('user_like')
            blog_like = serializer.validated_data.get('blog_like')
            # id blog and id user
            data_for_like = self.queryset.filter(blog_like=blog_like).filter(user_like=user_like)

            if(len(data_for_like) == 0):
                user_like = serializer.validated_data.get('user_like')
                blog_like = serializer.validated_data.get('blog_like')
                serializer.save(user_like=user_like, blog_like=blog_like)

                return Response({'key_message': 'Like' , 'status': status.HTTP_200_OK})
            else:
                data_for_like.delete()
                return Response({'key_message': 'Unlike' , 'status': status.HTTP_200_OK})

class GetLikeAll(generics.ListAPIView):
    queryset = ArticleLikeAndUnlike.objects.all()
    serializer_class = ArticleLikeAndUnlikeSerializer
    
    def get_queryset(self):
        """Return objects fot the current authenticated user only"""
        
        data = self.queryset.all()
        return data

    def list(self, request):
        queryset_list = self.get_queryset()
        serializer_list = ArticleLikeAndUnlikeSerializer(queryset_list, many=True)
        data = {'Like': serializer_list.data}
        return Response(data)


class GetLikeByIdApi(generics.ListAPIView):
    queryset = ArticleLikeAndUnlike.objects.all()
    serializer_class = ArticleLikeAndUnlikeSerializer

    def get_queryset(self):
        queryset = ArticleLikeAndUnlike.objects.filter(blog_like=self.kwargs['pk'])
        return queryset



# get blog user
class GetBlogAllUser(generics.ListAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = [ permissions.IsAuthenticated,]
    queryset = Blog.objects.all()
    serializer_class = BlogContentViewSerializer
    def get_queryset(self):
        """Return objects fot the current authenticated user only"""
        
        data = self.queryset.all()
        return data

    def list(self, request):
        queryset_list = self.get_queryset().order_by('-pub_date').filter(published=True).filter(own_user=self.request.user)
        serializer_list = BlogContentViewSerializer(queryset_list, many=True)
        data = {'blog': serializer_list.data}
        return Response(data)


class SearchBlogApi(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = SearchBlogSerialzer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['title', 'sub_title','content','own_user__first_name', 'own_user__last_name','category__name']