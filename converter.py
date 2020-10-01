print('How many kilometers did you cycle today?')
kms = input()
print('Ok, you said ' + kms + " "
      'kilometers, correct?')
miles = float(kms)/1.60934
miles = round(miles, 2)

# f  stands for function
print(f'Your {kms}km ride is equal to {miles} miles!')

# round()
