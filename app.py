import os
import logging
from flask import Flask, render_template, request, jsonify, flash, redirect, url_for
from flask_mail import Mail, Message

# Configure logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
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

# Blog routes
@app.route('/blog/web-development')
def blog_web_development():
    return render_template('blog_web_development.html')

@app.route('/blog/mobile-app-development')
def blog_mobile_app_dev():
    return render_template('blog_mobile_app_dev.html')

@app.route('/blog/graphic-design')
def blog_graphic_design():
    return render_template('blog_graphic_design.html')

@app.route('/blog/social-media-marketing')
def blog_social_media_marketing():
    return render_template('blog_social_media_marketing.html')

@app.route('/blog/video-editing')
def blog_video_editing():
    return render_template('blog_video_editing.html')

@app.route('/blog/content-writing')
def blog_content_writing():
    return render_template('blog_content_writing.html')

@app.route('/blog/branding-identity')
def blog_branding_identity():
    return render_template('blog_branding_identity.html')

@app.route('/blog/funnel-building')
def blog_funnel_building():
    return render_template('blog_funnel_building.html')

@app.route('/blog/ai-automation')
def blog_ai_automation():
    return render_template('blog_ai_automation.html')

@app.route('/blog/ai-chatbot')
def blog_ai_chatbot():
    return render_template('blog_ai_chatbot.html')

@app.route('/blog/advertisement-production')
def blog_advertisement_production():
    return render_template('blog_advertisement_production.html')

@app.route('/blog/ecommerce-development')
def blog_ecommerce_dev():
    return render_template('blog_ecommerce_dev.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
