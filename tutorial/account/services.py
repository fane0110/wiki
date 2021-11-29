
import grpc
from account.models import User
from account.serializers import UserProtoSerializer
from django_grpc_framework.services import Service

class userService(Service):
 serializer_class=UserProtoSerializer
 def get_object(self, pk):
        try:
              return User.objects.get(pk=pk)
        except User.DoesNotExist:
            self.context.abort(grpc.StatusCode.NOT_FOUND, 'User:%s not found!' % pk)

 def Retrieve(self, request, context):
        userdetail = self.get_object(request.id)
       
      
        serializer = UserProtoSerializer(userdetail)
        #print(serializer.message)
        return serializer.message