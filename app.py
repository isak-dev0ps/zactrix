import os
import logging
from flask import Flask, render_template, request, jsonify, flash, redirect, url_for
from flask_mail import Mail, Message

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

# Configure logging
logging.basicConfig(level=logging.DEBUG)

app.secret_key = os.environ.get("SESSION_SECRET", "dev-secret-key-change-in-production")

# Email configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_USERNAME')

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    try:
        # Get form data
        name = request.form.get('name')
        email = request.form.get('email')
        whatsapp = request.form.get('whatsapp')
        services = request.form.get('services')
        budget = request.form.get('budget')
        requirements = request.form.get('requirements')
        
        # Create email message
        msg = Message(
            subject=f'New Contact Form Submission from {name}',
            recipients=[os.environ.get('MAIL_USERNAME')],
            body=f"""
            New contact form submission:
            
            Name: {name}
            Email: {email}
            WhatsApp: {whatsapp}
            Services Needed: {services}
            Budget: ${budget}
            Requirements: {requirements}
            """
        )
        
        mail.send(msg)
        
        return jsonify({
            'success': True,
            'message': 'Thank you for your inquiry! We will get back to you soon.',
            'whatsapp_url': f"https://wa.me/7845603454?text=Hi Zactrix! I'm {name}, interested in {services}. My budget is ${budget}. {requirements}"
        })
        
    except Exception as e:
        logging.error(f"Error sending email: {str(e)}")
        return jsonify({
            'success': False,
            'message': 'There was an error submitting your form. Please try again. or contact on'
        }), 500

@app.route('/submit_enquiry', methods=['POST'])
def submit_enquiry():
    try:
        # Get form data
        name = request.form.get('name')
        whatsapp = request.form.get('whatsapp')
        budget = request.form.get('budget')
        message = request.form.get('message')
        service = request.form.get('service', 'General Inquiry')
        
        # Create email message
        msg = Message(
            subject=f'New Service Enquiry from {name} - {service}',
            recipients=[os.environ.get('MAIL_USERNAME')],
            body=f"""
            New service enquiry:
            
            Name: {name}
            WhatsApp: {whatsapp}
            Service: {service}
            Budget: ${budget}
            Message: {message}
            """
        )
        
        mail.send(msg)
        
        return jsonify({
            'success': True,
            'message': 'Enquiry submitted successfully!'
        })
        
    except Exception as e:
        logging.error(f"Error sending enquiry email: {str(e)}")
        return jsonify({
            'success': False,
            'message': 'There was an error submitting your enquiry. Please try again.'
        }), 500

