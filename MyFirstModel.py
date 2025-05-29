#Train a model to guess a comfortable boot size for a dog, based on the size of the harness that fits it.

import pandas as pd
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt

data = {
    'boot_size' : [ 39, 38, 37, 39, 38, 35, 37, 36, 35, 40,
                    40, 36, 38, 39, 42, 42, 36, 36, 35, 41,
                    42, 38, 37, 35, 40, 36, 35, 39, 41, 37,
                    35, 41, 39, 41, 42, 42, 36, 37, 37, 39,
                    42, 35, 36, 41, 41, 41, 39, 39, 35, 39
 ],
    'harness_size': [ 58, 58, 52, 58, 57, 52, 55, 53, 49, 54,
                59, 56, 53, 58, 57, 58, 56, 51, 50, 59,
                59, 59, 55, 50, 55, 52, 53, 54, 61, 56,
                55, 60, 57, 56, 61, 58, 53, 57, 57, 55,
                60, 51, 52, 56, 55, 57, 58, 57, 51, 59
                ]
}

# Convert into table
dataset=pd.DataFrame(data)
print(dataset)

# Define formula, boot_size is explained by harness_size
formula="boot_size ~ harness_size"

# Create model without to train it yet
model=smf.ols(formula=formula,data=dataset)
if not hasattr(model,'params'):
    print("Model selected but it does not have parameters set. We need to train it!")

# Train model
fitted_model=model.fit()

print(f'The following model parameters have been found')
print(f'Line slope {fitted_model.params.iloc[1]}')
print(f'Line intercept {fitted_model.params.iloc[0]}')

# Plot
plt.scatter(dataset['harness_size'],dataset['boot_size'])
plt.plot(dataset['harness_size'],fitted_model.params.iloc[1]*dataset['harness_size']+fitted_model.params.iloc[0],'r',label='Fitted line')

# Legends
plt.xlabel('harness_size')
plt.ylabel('boot_size')
plt.legend()

plt.show()

# Use model
harness_size={"harness_size":[52.5]}
# Predict
approx_boot_size=fitted_model.predict(harness_size)
print("Estimated approximate_boot_size:")
print(approx_boot_size[0])