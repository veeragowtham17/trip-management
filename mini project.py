#!/usr/bin/env python
# coding: utf-8

# In[3]:


import tkinter as tk
from tkinter import ttk, messagebox


class HolidayBookingApp:
    def __init__(self, master):
        self.master = master
        self.master.title("HOLIDAY Booking System")

        self.city_prices = {
            "Bangalore": {"adult": 0, "child": 0},
            "Kochi": {"adult": 0, "child": 0},
            "Hyderabad": {"adult": 0, "child": 0}
        }  # Prices for each city

        self.login_frame = tk.Frame(master)
        self.login_frame.grid(row=0, column=0, padx=10, pady=10)

        self.create_login_widgets()

    def create_login_widgets(self):
        self.username_label = tk.Label(self.login_frame, text="USERNAME:")
        self.username_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
        self.username_entry = tk.Entry(self.login_frame, width=30)
        self.username_entry.grid(row=0, column=1, padx=5, pady=5)

        self.password_label = tk.Label(self.login_frame, text="PASSWORD:")
        self.password_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
        self.password_entry = tk.Entry(self.login_frame, width=30, show="*")
        self.password_entry.grid(row=1, column=1, padx=5, pady=5)

        self.login_button = tk.Button(self.login_frame, text="Login", command=self.login)
        self.login_button.grid(row=2, column=1, padx=5, pady=5)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "admin" and password == "password":
            messagebox.showinfo("Login Successful", "Welcome")
            self.show_registration()  # Show registration frame after successful login
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    def show_registration(self):
        self.login_frame.grid_forget()
        self.registration_frame = tk.Frame(self.master)
        self.registration_frame.grid(row=0, column=0, padx=10, pady=10)
 
        self.name_label = tk.Label(self.registration_frame, text="Name:")
        self.name_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
        self.name_entry = tk.Entry(self.registration_frame, width=30)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        self.email_label = tk.Label(self.registration_frame, text="Email:")
        self.email_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
        self.email_entry = tk.Entry(self.registration_frame, width=30)
        self.email_entry.grid(row=1, column=1, padx=5, pady=5)

        self.mobile_label = tk.Label(self.registration_frame, text="Mobile:")
        self.mobile_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.E)
        self.mobile_entry = tk.Entry(self.registration_frame, width=30)
        self.mobile_entry.grid(row=2, column=1, padx=5, pady=5)

        self.age_label = tk.Label(self.registration_frame, text="Age:")
        self.age_label.grid(row=3, column=0, padx=5, pady=5, sticky=tk.E)
        self.age_entry = tk.Entry(self.registration_frame, width=30)
        self.age_entry.grid(row=3, column=1, padx=5, pady=5)

        self.passenger_count_label = tk.Label(self.registration_frame, text="Number of Passengers:")
        self.passenger_count_label.grid(row=4, column=0, padx=5, pady=5, sticky=tk.E)
        self.passenger_count_entry = tk.Entry(self.registration_frame, width=30)  # Entry for number of passengers
        self.passenger_count_entry.grid(row=4, column=1, padx=5, pady=5)

        self.passenger_details_button = tk.Button(self.registration_frame, text="Passenger Details", command=self.show_passenger_details)
        self.passenger_details_button.grid(row=5, column=1, padx=5, pady=5)

        # Lists to store passenger details
        self.passenger_details = []

    def show_passenger_details(self):
        passenger_count = self.passenger_count_entry.get()

        try:
            passenger_count = int(passenger_count)
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number for passengers.")
            return
        
        if passenger_count > 6:
            messagebox.showerror("Invalid Input", "Maximum number of passengers allowed is 6.")
            return

        # Clear existing widgets
        for widget in self.registration_frame.winfo_children():
            widget.destroy()

        # Add labels and entry fields for passenger details
        for i in range(passenger_count):
            passenger_frame = tk.Frame(self.registration_frame)
            passenger_frame.grid(row=i+1, column=0, columnspan=2, padx=5, pady=5)

            name_label = tk.Label(passenger_frame, text="Name:")
            name_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
            name_entry = tk.Entry(passenger_frame, width=25)
            name_entry.grid(row=0, column=1, padx=5, pady=5)

            age_label = tk.Label(passenger_frame, text="Age:")
            age_label.grid(row=0, column=2, padx=5, pady=5, sticky=tk.E)
            age_entry = tk.Entry(passenger_frame, width=5)
            age_entry.grid(row=0, column=3, padx=5, pady=5)

            gender_label = tk.Label(passenger_frame, text="Gender:")
            gender_label.grid(row=0, column=4, padx=5, pady=5, sticky=tk.E)
            gender_combobox = ttk.Combobox(passenger_frame, values=["Male", "Female", "Transgender"])
            gender_combobox.grid(row=0, column=5, padx=5, pady=5)

            # Append entry fields to the passenger details list
            self.passenger_details.append((name_entry, age_entry, gender_combobox))
            
        if len(self.passenger_details) == passenger_count:
            self.save_details_button = tk.Button(self.registration_frame, text="Save", command=self.save_passenger_details)
            self.save_details_button.grid(row=passenger_count+1, column=1, padx=5, pady=5)

    def save_passenger_details(self):
        # Additional validations can be added here if needed
        self.register_button = tk.Button(self.registration_frame, text="Register", command=self.register_user)
        self.register_button.grid(row=8, column=1, padx=5, pady=5)
        


    def register_user(self):
        # Validate passenger details
        for passenger in self.passenger_details:
            name_entry, age_entry, gender_entry = passenger
            name = name_entry.get()
            age = age_entry.get()
            gender = gender_entry.get()
            
            if not all([name, age, gender]):
                messagebox.showerror("Registration Failed", "Please fill in all passenger details.")
                return
            else:
                try:
                    age = int(age)
                except ValueError:
                    messagebox.showerror("Registration Failed", "Please enter a valid age for all passengers.")
                    return
       

        # If all validations pass, show success message
        messagebox.showinfo("Registration Successful", "User registered successfully!")
        self.hide_registration()
        self.show_booking_widgets()

    def hide_registration(self):
        self.registration_frame.grid_forget()

    def show_booking_widgets(self):
        self.booking_frame = tk.Frame(self.master)
        self.booking_frame.grid(row=1, column=0, padx=10, pady=10)

        self.label = tk.Label(self.booking_frame, text="Welcome to Holiday Booking")
        self.label.grid(row=0, column=0, columnspan=2)

        self.city_selected = tk.StringVar()
        self.flight_selected = tk.StringVar()
        self.hotel_selected = tk.StringVar()
        self.tourist_place_selected = tk.StringVar()  # Add variable to store selected tourist place

        self.city_options = ["Bangalore", "Kochi", "Hyderabad"]
        self.flight_options = ["Flight Bg", "Flight Kc", "Flight Hb"]
        self.hotel_options = ["Hotel 1", "Hotel 2", "Hotel 3"]

        self.city_label = tk.Label(self.booking_frame, text="Select City:")
        self.city_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
        self.city_menu = ttk.Combobox(self.booking_frame, textvariable=self.city_selected, values=self.city_options, 
                                   state="readonly", width=27)
        self.city_menu.bind("<<ComboboxSelected>>", self.update_tourist_places)  # Bind selection event
        self.city_menu.grid(row=1, column=1, padx=5, pady=5)

        self.flight_label = tk.Label(self.booking_frame, text="Select Flight:")
        self.flight_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.E)
        self.flight_menu = ttk.Combobox(self.booking_frame, textvariable=self.flight_selected, values=self.flight_options, 
                                     state="readonly", width=27)
        self.flight_menu.grid(row=2, column=1, padx=5, pady=5)

        self.hotel_label = tk.Label(self.booking_frame, text="Select Hotel:")
        self.hotel_label.grid(row=3, column=0, padx=5, pady=5, sticky=tk.E)
        self.hotel_menu = ttk.Combobox(self.booking_frame, textvariable=self.hotel_selected, values=self.hotel_options, 
                                    state="readonly", width=27)
        self.hotel_menu.grid(row=3, column=1, padx=5, pady=5)

        self.tourist_place_label = tk.Label(self.booking_frame, text="Select Tourist Place:")  # Add tourist place label
        self.tourist_place_label.grid(row=4, column=0, padx=5, pady=5, sticky=tk.E)
        self.tourist_place_menu = ttk.Combobox(self.booking_frame, textvariable=self.tourist_place_selected, 
                                            state="readonly", width=27)  # Add tourist place menu
        self.tourist_place_menu.grid(row=4, column=1, padx=5, pady=5)

        self.book_button = tk.Button(self.booking_frame, text="Book", command=self.show_payment_options)
        self.book_button.grid(row=5, column=1, padx=5, pady=5)
        
        self.back_button_booking = tk.Button(self.booking_frame, text="Back", command=self.show_registration)
        self.back_button_booking.grid(row=5, column=0, padx=5, pady=5)

    def update_tourist_places(self, event=None):
        selected_city = self.city_selected.get()
        if selected_city:
        # Assuming you have a dictionary of tourist places for each city
            tourist_places = {
                "Bangalore": ["Place 1", "Place 2", "Place 3", "Place 4"],
                "Kochi": ["Place A", "Place B", "Place C", "Place D"],
                "Hyderabad": ["Place X", "Place Y", "Place Z", "Place W"]
            }
        # Update tourist places based on the selected city
            self.tourist_place_menu['values'] = tourist_places[selected_city]
        else:
        # If no city is selected, clear the tourist place menu
            self.tourist_place_menu['values'] = []


    def calculate_fare_details(self, city):
    # Calculate total price in Indian rupees
        adult_price, child_price = self.calculate_prices(city)

    # Get the number of adults and children from the passenger details
        adults = sum(1 for p in self.passenger_details if int(p[1].get()) >= 6)
        children = sum(1 for p in self.passenger_details if int(p[1].get()) < 6)

    # Calculate total fare for adults and children
        total_adult_fare = adults * adult_price
        total_child_fare = children * child_price

        selected_flight = self.flight_selected.get()
        flight_fares = {"Flight Bg": 7000, "Flight Kc": 3800, "Flight Hb": 5200}
        total_flight_fare = flight_fares.get(selected_flight, 0)

        selected_hotel = self.hotel_selected.get()
        hotel_fares = {"Hotel 1": 3500, "Hotel 2": 2500, "Hotel 3": 3000}
        total_hotel_fare = hotel_fares.get(selected_hotel, 0)

    # Calculate total fare in USD and INR
        total_fare_usd = total_adult_fare + total_child_fare + total_flight_fare + total_hotel_fare
        exchange_rate = 1  # Assume exchange rate of 1 USD = 1 INR
        total_fare_inr = total_fare_usd * exchange_rate

    # Return the fare details
        return {
            "Adults": adults,
            "Children": children,
            "Adult Fare (₹)": adult_price,
            "Child Fare (₹)": child_price,
            "Total Adult Fare (₹)": total_adult_fare,
            "Total Child Fare (₹)": total_child_fare,
            "Flight Fare (₹)": total_flight_fare,
            "Hotel Fare (₹)": total_hotel_fare,
            "Total Fare": total_fare_inr
        }

    def show_payment_options(self):
    # Check if all necessary options are selected
        city = self.city_selected.get()
        flight = self.flight_selected.get()
        hotel = self.hotel_selected.get()

        if not all([city, flight, hotel]):
            messagebox.showerror("Booking Failed", "Please select city, flight, and hotel.")
            return

    # Calculate fare details
        fare_details = self.calculate_fare_details(city)

    # Construct the fare details message
        fare_message = "Fare Details:\n\n"
        for key, value in fare_details.items():
            fare_message += f"{key}: {value}\n"

    # Show fare details in a messagebox
        messagebox.showinfo("Fare Details", fare_message)
        
        self.proceed_to_payment(fare_details)


    def proceed_to_payment(self, fare_details):
        total_price_inr = fare_details["Total Fare"]  # Get total fare in INR from fare details

    # Remove existing widgets
        self.book_button.grid_forget()
        self.city_label.grid_forget()
        self.city_menu.grid_forget()
        self.flight_label.grid_forget()
        self.flight_menu.grid_forget()
        self.hotel_label.grid_forget()
        self.hotel_menu.grid_forget()
        self.tourist_place_label.grid_forget()  
        self.tourist_place_menu.grid_forget()

    # Show payment options
        self.payment_label = tk.Label(self.booking_frame, text="Select Payment Method:")
        self.payment_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)

    # Display payment options (ATM Card, UPI, Bank Transfer)
        self.payment_method = tk.StringVar()
        self.payment_method.set("ATM Card")  # Default payment method
        self.atm_radio = tk.Radiobutton(self.booking_frame, text="ATM Card", variable=self.payment_method, value="ATM Card")
        self.atm_radio.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

        self.upi_radio = tk.Radiobutton(self.booking_frame, text="UPI", variable=self.payment_method, value="UPI")
        self.upi_radio.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)

        self.bank_transfer_radio = tk.Radiobutton(self.booking_frame, text="Bank Transfer", variable=self.payment_method, value="Bank Transfer")
        self.bank_transfer_radio.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)

        self.pay_button = tk.Button(self.booking_frame, text="Pay Now (Total: ₹{})".format(total_price_inr), command=self.process_payment)
        self.pay_button.grid(row=4, column=1, padx=5, pady=5)
    def calculate_prices(self, city):
        # Your logic for calculating prices based on the selected city
        # Example implementation:
        city_prices = {
            "Bangalore": {"adult": 2500, "child": 1100},
            "Kochi": {"adult": 1500, "child": 950},
            "Hyderabad": {"adult": 2000, "child": 1000}
        }
        if city in city_prices:
            return city_prices[city]["adult"], city_prices[city]["child"]
        else:
            # Return default prices if city is not found
            return 0, 0

    def process_payment(self):
        payment_method = self.payment_method.get()

        if payment_method == "ATM Card":
            self.show_atm_payment()
        elif payment_method == "UPI":
            self.show_upi_payment()
        elif payment_method == "Bank Transfer":
            self.show_bank_transfer_payment()

    def show_atm_payment(self):
        self.payment_window = tk.Toplevel(self.master)
        self.payment_window.title("ATM Payment")

        self.card_number_label = tk.Label(self.payment_window, text="Card Number:")
        self.card_number_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
        self.card_number_entry = tk.Entry(self.payment_window, width=30)
        self.card_number_entry.grid(row=0, column=1, padx=5, pady=5)

        self.card_holder_label = tk.Label(self.payment_window, text="Card Holder Name:")
        self.card_holder_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
        self.card_holder_entry = tk.Entry(self.payment_window, width=30)
        self.card_holder_entry.grid(row=1, column=1, padx=5, pady=5)

        self.expiry_label = tk.Label(self.payment_window, text="Expiry Date (MM/YY):")
        self.expiry_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.E)
        self.expiry_entry = tk.Entry(self.payment_window, width=10)
        self.expiry_entry.grid(row=2, column=1, padx=5, pady=5)

        self.cvv_label = tk.Label(self.payment_window, text="CVV:")
        self.cvv_label.grid(row=3, column=0, padx=5, pady=5, sticky=tk.E)
        self.cvv_entry = tk.Entry(self.payment_window, width=10)
        self.cvv_entry.grid(row=3, column=1, padx=5, pady=5)

        self.confirm_button = tk.Button(self.payment_window, text="Confirm", command=self.process_atm_payment)
        self.confirm_button.grid(row=4, column=1, padx=5, pady=5)

    def show_upi_payment(self):
        self.payment_window = tk.Toplevel(self.master)
        self.payment_window.title("UPI Payment")

        self.upi_id_label = tk.Label(self.payment_window, text="UPI ID:")
        self.upi_id_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
        self.upi_id_entry = tk.Entry(self.payment_window, width=30)
        self.upi_id_entry.grid(row=0, column=1, padx=5, pady=5)

        self.confirm_button = tk.Button(self.payment_window, text="Proceed", command=self.show_upi_pin_entry)
        self.confirm_button.grid(row=1, column=1, padx=5, pady=5)

    def show_upi_pin_entry(self):
        upi_id = self.upi_id_entry.get()
        if upi_id:
            self.upi_id_entry.config(state="disabled")
            self.upi_pin_label = tk.Label(self.payment_window, text="UPI PIN:")
            self.upi_pin_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.E)
            self.upi_pin_entry = tk.Entry(self.payment_window, width=30, show="*")
            self.upi_pin_entry.grid(row=2, column=1, padx=5, pady=5)

            self.confirm_button.config(command=self.process_upi_payment, text="Confirm")
        else:
            messagebox.showerror("Payment Failed", "Please enter UPI ID to proceed.")

    def show_bank_transfer_payment(self):
        self.payment_window = tk.Toplevel(self.master)
        self.payment_window.title("Bank Transfer")

        self.account_number_label = tk.Label(self.payment_window, text="Account Number:")
        self.account_number_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
        self.account_number_entry = tk.Entry(self.payment_window, width=30)
        self.account_number_entry.grid(row=0, column=1, padx=5, pady=5)

        self.ifsc_label = tk.Label(self.payment_window, text="IFSC Code:")
        self.ifsc_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
        self.ifsc_entry = tk.Entry(self.payment_window, width=30)
        self.ifsc_entry.grid(row=1, column=1, padx=5, pady=5)

        self.confirm_button = tk.Button(self.payment_window, text="Confirm", command=self.process_bank_transfer_payment)
        self.confirm_button.grid(row=2, column=1, padx=5, pady=5)

    def process_atm_payment(self):
    # Get values from the entry fields
        card_number = self.card_number_entry.get()
        card_holder_name = self.card_holder_entry.get()
        expiry_date = self.expiry_entry.get()
        cvv = self.cvv_entry.get()

    # Check if any field is empty
        if not all([card_number, card_holder_name, expiry_date, cvv]):
            messagebox.showerror("Payment Failed", "Please fill in all the fields.")
            return

    # Placeholder function for processing ATM payment
        messagebox.showinfo("Payment Processed", "ATM payment processed successfully.")
        self.payment_window.destroy()

    def process_upi_payment(self):
        upi_pin = self.upi_pin_entry.get()

    # Check if the entered PIN is either 4 or 6 digits
        if len(upi_pin) not in [4, 6]:
            messagebox.showerror("Payment Cancelled", "Invalid UPI PIN. Payment cancelled.")
            return
        # Placeholder function for processing UPI payment
        messagebox.showinfo("Payment Processed", "UPI payment processed successfully.")
        self.payment_window.destroy()

    def process_bank_transfer_payment(self):
        account_number = self.account_number_entry.get()
        ifsc_code = self.ifsc_entry.get()
    
    # Check if both account number and IFSC code are entered
        if not all([account_number, ifsc_code]):
            messagebox.showerror("Payment Failed", "Please fill in all the fields.")
            return

    # Placeholder function for processing Bank Transfer payment
        messagebox.showinfo("Payment Processed", "Bank Transfer payment processed successfully.")
        self.payment_window.destroy()
    def save_payment_details(self):
    # Get passenger details from the DataFrame
        passenger_details = {
            "Name": [passenger[0].get() for passenger in self.passenger_details],
            "Age": [int(passenger[1].get()) for passenger in self.passenger_details],
            "Gender": [passenger[2].get() for passenger in self.passenger_details]
        }

    # Add the paid amount
        passenger_details["Paid Amount"] = self.calculate_fare_details(self.city_selected.get())["Total Fare"]

    # Create a DataFrame from the data
        payment_df = pd.DataFrame(passenger_details)

    # Save the DataFrame to an Excel file
        payment_df.to_excel("payment_details.xlsx", index=False)

def main():
    root = tk.Tk()
    app = HolidayBookingApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:




