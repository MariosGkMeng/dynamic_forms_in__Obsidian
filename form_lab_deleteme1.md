
%% 
CODE WEAKNESSES
--

1. Explicit fields:
	1. Sections such as "# Parameters" should not have their names changed, since the "cover_letter_lab.py" uses this name to recognise where the lines containing the parameters start
	2. symbols: 
		1. symbols such as  "🏁,💬,⚙,🗝" need to be explicitly added in  "cover_letter_lab.py" (in `par['words_pattern']`), since I don't know how to categorise them using the regural-expression shortcuts!
		2. CORRECT **USAGE OF SYMBOLS**: 
			1. #🔰/par: this type of parameter is filled either from  "cover_letter_lab.py" based on the table of saved job positions, or by hand
			2. #🏁/par: user-set constant
			3. #❓/bvar: boolean variable
			4. #🗝/var: variable
				1. You write an expression in a Pythonic way: `exec(expression)` using only `[+, -, \*, \==]` as operators
2. Parameters of type " #🔰/par " that are automaticaally filled by  "cover_letter_lab.py" should match the exact names of those fields in the [[tableJobs#Saved Positions]] (set in variable 'flds2change')
3. **SYNTAX** in expressions
	1. There should always be at least one whitespace between operators, parameters and parantheses. E.g.: `exec( #❓/is_research \* #❓/is_company )` is the correct syntax. To write `exec( #❓/is_research \* #❓/is_company)`, `exec( #❓/is_research\* #❓/is_company )` would be incorrect
	2. For an empty expression, use "' '" instead of "''"

%%




[[table_deleteme1]]




# [[form_deleteme1]]	


 [Generate](<file:///C:\MARIOS\WORK\AUTOMATIONS\generate_Letter.bat>)
==


# FormID: 1

# Parameters
|                      par | val                                                                                             |
| ------------------------:|:----------------------------------------------------------------------------------------------- |
|         #🔰/Product_type | #🔅/Car |
|              #🔰/Country | #🏁/🕊/DE |
|         #🏁/LAW__british | British production laws apply                                                                   |
|              #🏁/LAW__EU | European Union production laws apply                                                            |
|            #🏁/LAW__Asia | East Asia  production laws apply                                                                |
| #🏁/⚠__hazardous_product | This is a hazardous product. Failure to comply with corresponding laws can lead to time in jail | 


# Fields

|                     Field | Value                                                                                                                    |
| -------------------------:|:------------------------------------------------------------------------------------------------------------------------ |
|            #❓/made_in_EU | exec( ( #🔰/Country \== #🏁/🕊/NOR  ) + ( #🔰/Country \== #🏁/🕊/DE ) )                                                    |
|          #❓/made_in_Asia | exec( ( #🔰/Country \== #🏁/🕊/China   ) + ( #🔰/Country \== #🏁/🕊/India ) )                                              |
|       #❓/made_in_Britain | exec( ( #🔰/Country \== #🏁/🕊/EN   )  )                                                                                  |
|             #🗝/LAWS_apply | exec( #🏁/LAW__british \* #❓/made_in_Britain + #🏁/LAW__Asia  \* #❓/made_in_Asia  + #🏁/LAW__EU  \* #❓/made_in_EU   ) |
| #❓/PRODUCT__is_hazardous | exec( ( #🔰/Product_type \==  #🔅/Gun ) )                                                                                |
|   #🗝/⚠__hazardous_product | exec( #🏁/⚠__hazardous_product  \* #❓/PRODUCT__is_hazardous + ( ' ' )  \* ( 1 - #❓/PRODUCT__is_hazardous ) )           |
|                  #🗝/debug | exec( 1 - #❓/PRODUCT__is_hazardous )                                                                                    |


 [Generate](<file:///C:\MARIOS\WORK\AUTOMATIONS\generate_Letter.bat>)
==

[[form_deleteme1]]	


# Main

This is a very simple dynamic form. 

To produce this product, #🗝/LAWS_apply. Please read the corresponding cite. #🗝/⚠__hazardous_product

