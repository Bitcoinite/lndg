from rest_framework import serializers
from .models import Payments, Invoices, Forwards, Channels, Rebalancer

##FUTURE UPDATE 'exclude' TO 'fields'

class PaymentSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Payments
        exclude = []

class InvoiceSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Invoices
        exclude = []

class ForwardSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Forwards
        exclude = []

class ChannelSerializer(serializers.HyperlinkedModelSerializer):
    chan_id = serializers.ReadOnlyField()
    class Meta:
        model = Channels
        exclude = []

class RebalancerSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    requested = serializers.ReadOnlyField()
    start = serializers.ReadOnlyField()
    stop = serializers.ReadOnlyField()
    status = serializers.ReadOnlyField()
    class Meta:
        model = Rebalancer
        exclude = []

class ConnectPeerSerializer(serializers.Serializer):
    peer_pubkey = serializers.CharField(label='peer_pubkey', max_length=66)
    host = serializers.CharField(label='host', max_length=120)

class OpenChannelSerializer(serializers.Serializer):
    peer_pubkey = serializers.CharField(label='peer_pubkey', max_length=66)
    local_amt = serializers.IntegerField(label='local_amt')
    sat_per_byte = serializers.IntegerField(label='sat_per_btye')

class CloseChannelSerializer(serializers.Serializer):
    funding_txid = serializers.CharField(label='funding_txid', max_length=64)
    output_index = serializers.IntegerField(label='output_index')
    target_fee = serializers.IntegerField(label='target_fee')
    force = serializers.BooleanField(default=False)

class AddInvoiceSerializer(serializers.Serializer):
    value = serializers.IntegerField(label='value')