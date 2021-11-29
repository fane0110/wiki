from django_grpc_framework import proto_serializers
from account.models import User
from account_proto import account_pb2
from account.models import User,Cryptamount
from rest_framework.serializers import SerializerMethodField
from google.protobuf.json_format import MessageToDict, ParseDict


class UserProtoSerializer(proto_serializers.ModelProtoSerializer):
   
    cryptamount = SerializerMethodField()
  

    print(cryptamount)
    class Meta:
        model = User
        proto_class = account_pb2.User
        fields = ['id', 'username', 'email','cryptamount']
    def message_to_data(self, message):
        """Protobuf message -> Dict of python primitive datatypes.
        """
        return MessageToDict(
            message, including_default_value_fields=True,
            preserving_proto_field_name=True
        )

    def data_to_message(self, data):
        """Protobuf message <- Dict of python primitive datatypes."""
        return ParseDict(
            data, self.Meta.proto_class(),
            ignore_unknown_fields=False
        )
    def get_cryptamount(self, obj):
        try:
           
            Cryptamount_contents = Cryptamount.objects.all().select_related('cryptid').filter(User = User.objects.get(id=obj.id))
            
            Cryptamount_contents= list(Cryptamount_contents.values("amount","cryptid__cryptname"))
            
        
            return Cryptamount_contents
        except:
            Cryptamount_contents = None
            return Cryptamount_contents
    