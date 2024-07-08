from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CompanySerializer, BuyerSerializer, DealSerializer
from .models import Company, Buyer, Deal

# Create your views here.

class CompanyListAPIView(APIView):
    def get(self, request):
        name = request.query_params.get('name', None)
        companies = Company.objects.all()
        if name:
            companies = companies.filter(name__icontains=name)
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CompanyCreateAPIView(APIView):
    def post(self, request):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BuyerListAPIView(APIView):
    def get(self, request):
        name = request.query_params.get('name', None)
        buyers = Buyer.objects.all()
        if name:
            buyers = buyers.filter(name__icontains=name)
        serializer = BuyerSerializer(buyers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class BuyerCreateAPIView(APIView):
    def post(self, request):
        serializer = BuyerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DealListAPIView(APIView):
    def get(self, request):
        deal_date = request.query_params.get('deal_date', None)
        buyer_id = request.query_params.get('buyer_id', None)
        company_id = request.query_params.get('company_id', None)
        deals = Deal.objects.all()
        if deal_date:
            deals = deals.filter(deal_date=deal_date)
        if buyer_id:
            deals = deals.filter(buyer_id=buyer_id)
        if company_id:
            deals = deals.filter(company_id=company_id)
        serializer = DealSerializer(deals, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class DealCreateAPIView(APIView):
    def post(self, request):
        serializer = DealSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)