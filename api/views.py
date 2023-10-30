from .models import *
from .serializers import *
from .permissions import *
from decouple import config
from users.models import ChefUser
from django.core.mail import send_mail
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class ChefListView(generics.ListAPIView):
    queryset = ChefUser.objects.all()
    serializer_class = ChefSerializer

class ChefDishesListView(generics.RetrieveAPIView):
    queryset = ChefUser
    serializer_class = ChefListSerializer
    lookup_field = 'pk'

class DishListView(generics.ListAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    permission_classes = []
    authentication_classes = []

class DishByIdView(generics.RetrieveAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    authentication_classes = []
    permission_classes = []
    lookup_field = 'id'

class DishListCreateView(generics.CreateAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    permission_classes = [IsAuthenticated, IsChef]

class DishUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    permission_classes = [IsAuthenticated, IsChef]

class ContactView(APIView):
    permission_classes = []
    def post(self, request, *args, **kwargs):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data['name']
            email = serializer.validated_data['email']
            message = serializer.validated_data['message']
            subject = f"Contact from {name}"
            email_message = f'Name: {name}\nEmail: {email}\nMessage:\n{message}'
            recipients = config('RECIPIENTS').split(',')
            try:
                send_mail(subject, email_message, email, recipients)
                return Response({'message': 'Email sent successfully.'}, status=status.HTTP_200_OK)
            except:
                return Response({'error': 'Failed to send message.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class DishListState(generics.ListAPIView):
    queryset = Dish.objects.all()
    permission_classes = []
    authentication_classes = []
    serializer_class = DishSerializer

    def post(self, request):
        state=request.data['popularity_state']
        try:
            dishes = Dish.objects.filter(popularity_state=state)
            serializer = DishSerializer(dishes, many=True)
            return Response({'data':serializer.data}, status=status.HTTP_200_OK)
        except Dish.DoesNotExist:
            return Response({'message':'Data does not exist.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'err':str(e), 'serializer_errors':serializer.error_messages})

class DishListCourse(generics.ListAPIView):
    permission_classes = []
    authentication_classes = []
    def post(self, request):
        course = request.data['course']
        try:
            dishes = Dish.objects.filter(main_course_starter_dessert=course)
            serializer = DishSerializer(dishes, many=True)
            return Response({'data':serializer.data}, status=status.HTTP_200_OK)
        except Dish.DoesNotExist:
            return Response({'message':'Dish does not exist.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'err':str(e), 'serializer_errors':serializer.error_messages}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class DishListChoice(generics.ListAPIView):
    permission_classes = []
    authentication_classes = []
    def post(self, request):
        choice = request.data['choice']
        try:
            dishes = Dish.objects.filter(veg_non_veg=choice)
            serializer = DishSerializer(dishes, many=True)
            return Response({'data':serializer.data}, status=status.HTTP_200_OK)
        except Dish.DoesNotExist:
            return Response({'message':'Dish does not exist'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'err':str(e), 'serializer_errors':serializer.error_messages}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class DishListIngredients(generics.ListAPIView):
    permission_classes = []
    authentication_classes = []

    def post(self, request):
        ingredients = request.data['ingredients']
        dishes = []
        for ingredient in ingredients:
            try:
                dishes.extend(Dish.objects.filter(ingredients__name=ingredient))
            except:
                pass
        serializer = DishSerializer(dishes, many=True)
        return Response({'data':serializer.data}, status=status.HTTP_200_OK)
    