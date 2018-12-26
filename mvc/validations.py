def validateprescence(username):
    if not username or username.isspace() or len(username)<2 or len(username)>24:
        return "please enter username"
    return False

def validate_data(value, lst):
	if value not in lst:
		return 'field must be present' 
    
