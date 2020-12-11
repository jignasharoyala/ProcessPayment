from flask import jsonify, request
from flask_restful import Resource
import re
class ProcessPayment(Resource):

    def get(self):
        return {'status': 'bad request', 'data': 'get method not allow'}, 400

    def post(self):

        try:
            
            json_data = request.get_json(force=True)
            if not json_data:
                   return {'message': 'No input data provided'}, 400
          
            creditCardNumber = json_data['CreditCardNumber']
            cardHolder = json_data['CardHolder']
            expirationDate = json_data['ExpirationDate']
            securityCode = json_data['SecurityCode']
            amount = json_data['Amount']
           
            if creditCardNumber:
                number_validated = validCreditCrads(creditCardNumber)
                if number_validated == 0 :
              
                    return {'status': 'bad request', 'data': 'Enter valid card number'}, 400

            else:

                return {'status': 'bad request', 'data': 'CreditCardNumber field required'}, 400

            if cardHolder:

                valid_holder_name = validCardHolder(validCardHolder)

                if valid_holder_name == 0:
                    return {'status': 'bad request', 'data': 'Enter valid Card Holder Name'}, 400
                

            if expirationDate:

                valid_date = validExpirationDate(expirationDate)
                if valid_date == 0:
                    return {'status': 'bad request', 'data': 'Enter valid expiration Date'}, 400    
            else:
                return {'status': 'bad request', 'data': 'ExpirationDate field required'}, 400


            if securityCode:

                valid_code = validSecurityCode(securityCode)
                if valid_code == 0:
                    return {'status': 'bad request', 'data': 'Enter valid security code'}, 400    
            else:
                return {'status': 'bad request', 'data': 'SecurityCode field required'}, 400      

            if amount:
                valid_amout = validAmout(amount)
                if valid_amout == 0:
                    return {'status': 'bad request', 'data': 'Enter valid amout'}, 400    

            else:
                return {'status': 'bad request', 'data': 'Amount field required'}, 400                


            payment_method = getPaymentMetho(amount)
            if payment_method == "CheapPaymentGateway":
                return {'status': 'sucess', 'data': 'Payment is processed'}, 200

            elif payment_method == "ExpensivePaymentGateway":
                return {'status': 'sucess', 'data': {'message': 'Payment is processed', 'retry': 1}}, 200           
           
            elif payment_method == "PremiumPaymentGatewa":

                return {'status': 'sucess', 'data': {'message': 'Payment is processed', 'retry': 3}}, 200           
            
            else:
                return {'status': 'error', 'data': 'internal server error'}, 500
        except Exception as e:
            
            return {'status': 'error', 'data': 'internal server error'}, 500
            




def validCreditCrads(creditCardNumber):

    if re.match(r"^[456]([\d]{15}|[\d]{3}(-[\d]{4}){3})$", creditCardNumber) and not re.search(r"([\d])\1\1\1", creditCardNumber.replace("-", "")):
        return 1
    else:
        return 0
    

def validCardHolder(cardHolder):

    if type(test_string) == str:
        return 1
    else:
        return 0


def validExpirationDate(expirationDate):

    from datetime import datetime 
    if re.match(r"^(0[1-9]|1[0-2])\/?([0-9]{4}|[0-9]{2})$", expirationDate):
        
        exp_date = datetime.strptime(expirationDate, '%b %d %Y %I:%M%p')

        if exp_date < datetime.datetime.now():
            return 1
        else:
            return 0
    else:
        return 0
    

def validSecurityCode(securityCode):

    if len(SecurityCode) == 3:
        return 1
    else:
        return 0


def validAmout(amount):
    if amount.isdecimal() and float(amount) > 0:
        return 1
    else:
        return 0


def getPaymentMethod(amount):
    if float(amount)< 20:
        return "CheapPaymentGateway"
    elif float(amount)> 20 and float(amount) < 500:
        return "ExpensivePaymentGateway"
    else:
        return "PremiumPaymentGatewa"
