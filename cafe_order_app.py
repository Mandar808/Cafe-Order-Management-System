import streamlit as st

# Menu dictionary with items and their prices
menu = {
    'Pasta': 40,
    'Pizza': 50,
    'Burger': 60,
    'Salad': 70,
    'Coffee': 80,
}

# Initialize session state variables if they don't exist
if 'ordered_items' not in st.session_state:
    st.session_state.ordered_items = []
if 'order_total' not in st.session_state:
    st.session_state.order_total = 0

# Streamlit app layout
st.title('Cafe Order Management System')
st.subheader('Menu')
for item, price in menu.items():
    st.write(f"{item}: Rs {price}")

# Function to add items to order
def add_item_to_order(item):
    if item in menu:
        st.session_state.ordered_items.append(item)
        st.session_state.order_total += menu[item]
        st.success(f"{item} added to your order")
    else:
        st.error(f"{item} is not available")

# Input form for ordering items
st.subheader('Order Items')
item = st.text_input('Enter the name of the item you want to order')
if st.button('Add to Order'):
    add_item_to_order(item)

# Display current order and total
if st.session_state.ordered_items:
    st.subheader('Your Order')
    for ordered_item in st.session_state.ordered_items:
        st.write(ordered_item)
    st.subheader(f"Total Amount: Rs {st.session_state.order_total}")

# Option to quit or add more items
st.subheader('Add More Items or Quit')
another_order = st.radio("Do you want to add another item?", ('Yes', 'No'))
if another_order == 'No':
    st.write("Thank you for your order!")
