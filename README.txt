# Discount Model v4

This repo contains a trained Decision Tree model to estimate the maximum safe discount for a sales line item.

### Features used:
- sub-category
- original_sales_price
- cost_pp
- discount_pct

### Files:
- `discount_model_v4.pkl`: Trained model
- `label_encoders_v4.pkl`: Label encoder for 'sub-category'
- `requirements.txt`: Python dependencies
- `README.txt`: Description and usage

### Use Case:
Given a sales context, loop through possible discounts and use the model to find the highest discount that still predicts a profitable outcome.
