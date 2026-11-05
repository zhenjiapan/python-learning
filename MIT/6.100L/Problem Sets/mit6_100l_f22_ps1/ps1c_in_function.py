def part_c(initial_deposit):
	#########################################################################
	cost_of_dream_home = 800000
	portion_down_payment = 0.25
	months = 36
	high = 1
	low = 0
	r = (high + low)/2
	amount_saved = initial_deposit * (1 + r/12) ** months
	steps = 1
	
	##################################################################################################
	## Determine the lowest rate of return needed to get the down payment for your dream home below ##
	##################################################################################################
	if initial_deposit >= cost_of_dream_home*portion_down_payment:
	    r = 0.0
	elif initial_deposit * (1 + 1/12) ** months < cost_of_dream_home*portion_down_payment:
	    r = None
	    steps = 0
	else:
	    while abs(amount_saved - cost_of_dream_home*portion_down_payment) >= 100:
	        if amount_saved > cost_of_dream_home*portion_down_payment:
	            high = r
	        else:
	            low = r
	        r = (high + low)/2
	        amount_saved = initial_deposit * (1 + r / 12) ** months
	        steps += 1
	print('Best savings rate:',r,'[or very close to this number]')
	print('Steps in bisection search:',steps,'[or very close to this number]')
	return r, steps