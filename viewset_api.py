from drink_store models kelompok
from drink_store serializers import.kelompok serializers
from rest_framework viewsets

class kelompokViewset(viewsets.ModelViewSet);
queryset = kelompok.objects.all()
serializers_class =kelompokSerializer

