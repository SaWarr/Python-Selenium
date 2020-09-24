require "selenium-webdriver"
require "rspec"
require "ffi"

# TEST: Log in and shop
describe "Shop application" do
    describe "Login to the shop application" do

# Commented out redundant 
#        it "Confirms entry field for uername" do
#            driver = Selenium::WebDriver.for :firefox
#            # Go to login form
#            driver.navigate.to "https://insertshoppingapphere"
#            username_field = driver.find_element(id: 'user_username')
#            username_field.send_keys("user")
#            expect(username_field). to eq("user")
#            driver.quit
#        end

#        it "Confirms entry field for password" do
#            driver = Selenium::WebDriver.for :firefox
#            # Go to login form
#           driver.navigate.to "https://insertshoppingapphere"
#            password_field = driver.find_element(id: 'user_password')
#            password_field.send_keys("drowssap")
#            expect(password_field). to eq("drowssap")
#            driver.quit
#        end
        
        it "Confirm that a user can login" do
            driver = Selenium::WebDriver.for :firefox
            # Go to signup form
            driver.navigate.to "https://insertshoppingapphere"
            # Fill out and submit form
            username_field = driver.find_element(id: 'user_username')
            username_field.send_keys("user")
  
            email_field = driver.find_element(id: 'user_email')
            email_field.send_keys("user@test.com")
  
            password_field = driver.find_element(id: 'user_password')
            password_field.send_keys("drowssap")
  
            login_button = driver.find_element(id: 'submit')
            login_button.click
  
            # Confirm user is signed in successfully
            banner = driver.find_element(id: 'flash_success')
            banner_text = banner.text
            expect(banner_text).to eq("Welcome to the store")
  
            driver.quit
        end
    end

    describe "Shopping scenarios" do
        it "Does shopping things" do
            # Different shopping things
        end
    end

    describe "Basket scenarios" do
        it "Does basket things" do
            # Different basket things
        end
    end

    describe "Post checkout" do
        it "Does a confirmation screen with link back to log in" do
            # Simple path to logout
        end
    end

end
