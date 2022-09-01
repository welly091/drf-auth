from .models import Preorder
from .serializers import PreorderSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .permissions import IsOwnerOrReadOnly

class PreorderListView(ListCreateAPIView):
    queryset = Preorder.objects.all()
    serializer_class = PreorderSerializer

class PreorderDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Preorder.objects.all()
    serializer_class = PreorderSerializer