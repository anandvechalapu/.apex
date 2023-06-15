@app.route('/check_spouse_insurance_eligibility', methods=['POST'])
def check_spouse_insurance_eligibility():
  data = request.get_json()
  spouse_data = data['spouse_data']
  # Fetch spouse data from bank system (including verified DOB and CRIF) if available
  if spouse_data['dob'] == verified_dob and spouse_data['crif'] == verified_crif:
    # Check eligibility of both members
    if eligibility_check(data['member_data']) == True and eligibility_check(spouse_data) == True:
      # Assign minimum sum assured of 50k if no credit score is provided
      if spouse_data['credit_score'] == 0:
        min_sum_assured = 50000
      else:
        # Calculate minimum sum assured based on the credit score
        min_sum_assured = calculate_min_sum_assured(spouse_data['credit_score'])
      # Check product and master level boundary conditions
      if min_sum_assured >= product_min_sum_assured and min_sum_assured <= product_max_sum_assured and spouse_data['age'] >= master_min_age and spouse_data['age'] <= master_max_age:
        # Spouse eligible for insurance cover
        return jsonify({'status': 'success', 'message': 'Spouse eligible for insurance cover'})
      else:
        # Spouse not eligible for insurance cover
        return jsonify({'status': 'failure', 'message': 'Spouse not eligible for insurance cover'})
    else:
      # Spouse not eligible for insurance cover
      return jsonify({'status': 'failure', 'message': 'Spouse not eligible for insurance cover'})
  else:
    # Provide easy-to-use Ekyc/Ckyc interface for inputting spouse data
    return jsonify({'status': 'failure', 'message': 'Spouse data not available. Please provide Ekyc/Ckyc data.'})