from models.budget_model import Budget
from flask import Blueprint, jsonify, request, abort
from request_util import Request_Util

budget_endpoint = Blueprint('budget_endpoint',
                                __name__)

# A GET endpoint to get all the budgets
@budget_endpoint.route('/budgets', methods=['GET'])
def get_all_budgets():
    return Request_Util.basic_get_request(Budget)

# A POST endpoint to create a new budget
@budget_endpoint.route('/budgets', methods=['POST'])
def create_resource():
    body = Request_Util.get_body(request)

    number = body.get('number')
    task_area = body.get('task_area')
    ceiling_value = body.get('ceiling_value')
    funded_value = body.get('funded_value')
    eac_revenue = body.get('eac_revenue')
    eac_profit = body.get('eac_profit')
    eac_profit_percent = body.get('eac_profit_percent')
    new_budget = Budget(number, name, size,
                                status, length, dependency)
    return Request_Util.basic_post_request(new_budget)

# A DELETE endpoint to delete a budget
@budget_endpoint.route('/budgets/<budget_id>', 
                         methods=['DELETE'])
def delete_project(budget_id):
    return Request_Util.basic_delete_request(Budget, 
                                        budget_id)