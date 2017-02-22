def char_swap(string): 	#Here we define function change_char which accepts one variable, string
    first = string[0]   #first is a variable to store the first character of the string

    for x in string:
        string = string.replace(first, '$')	#this replaces every occurence of letters similar to the first
        string = first + string[1:]		#this replacesthe firs "$" with our first character from earlier on
    return string				#this returns the string from the previous step

user_input=raw_input("Enter your word of choice: \n")		#this takes in input from the user
print (char_swap(user_input))					#this prints the result of function char_swap with user_input as the variable replacing string
