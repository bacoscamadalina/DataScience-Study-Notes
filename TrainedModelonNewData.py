import pandas as pd
import statsmodels.formula.api as smf
import joblib

'''
We want to train the model just once, then load that model onto the server that runs our online store.
Although the model is trained on a dataset we downloaded from the internet, we actually want to use it to estimate 
the boot size of our customers' dogs who aren't in this dataset!
'''

#Load dataset and print first 5 rows
data = pd.read_csv('doggy_boot_harness.csv')
print(data.head())

# Create and train a model
'''
This model finds a linear relationship between boot size and harness size, which we can use later to predict a dog's
boot size, given their harness size
'''
model = smf.ols(formula='boot_size ~ harness_size', data=data).fit()
print('Model trained!')

# Save and load a model
model_filename='.avalanche_dog_boot_model.pkl'
joblib.dump(model, model_filename)
print('Model saved!')

# Load model
model_loaded = joblib.load(model_filename)
print("We have loaded a model with the following parameters:")
print(model_loaded.params)

# Put it together
'''
This function loads a pretrained model. It uses the model with the customer's dog's harness size to predict the size of
boots that will fit that dog.
'''
def load_model_and_predict(harness_size):
    # Load the model from file and prin basic information about it
    loaded_model = joblib.load(model_filename)
    print("We have loaded a model with the following parameters:")
    print(model_loaded.params)

    # Prepare data for the model
    inputs={'harness_size':[harness_size]}

    #Use model to make a prediction
    pred_boot_size=loaded_model.predict(inputs)[0]
    return pred_boot_size

# Practice using model
pred_boot_size=load_model_and_predict(45)
print("Predicted dog boot size:", pred_boot_size)

# This function warns customers if the dog boots they selected are the right size
def check_size_of_boots(selected_harness_size,selected_boot_size):
    '''
    Checks if the selected boot size matches the expected size based on the harness size.
    selected_harness_size: The size of the harness the customer wants to buy
    selected_boot_size: The size of the doggy boots the customer wants to buy
    '''
    #Estimate boot size
    estimated_boot_size=load_model_and_predict(selected_harness_size)

    # Round to the nearest whole number
    estimated_boot_size=int(round(estimated_boot_size))

    # Check if the boot size is appropriate
    if selected_boot_size == estimated_boot_size:
        print("The selected boots are probably ok!")
    elif selected_boot_size < estimated_boot_size:
        print(f"The selected boots are probably too small! We recommend size: {estimated_boot_size}")
    else:
        print(f"The selected boots are probably too big! We recommend size: {estimated_boot_size}")

# Practice using our new warning system
check_size_of_boots(selected_harness_size=55, selected_boot_size=39)

