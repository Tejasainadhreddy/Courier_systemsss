from app import app, db
from models import Officer, User, Branch, Driver, Courier, CourierTrack

with app.app_context():
    db.create_all()
    
    if not Officer.query.filter_by(officer_name='Team_7').first():
        db.session.add(Officer(officer_name='Team_7', off_pwd='password7', level=1))
    
    if not User.query.filter_by(email='sriram@csueb.edu').first():
        u = User(fullname='Sriram Kumar', email='sriram@csueb.edu', password='password123', 
                 phone='510-885-3000', address='25800 Carlos Bee Blvd, Hayward, CA')
        db.session.add(u)
    
    if not Branch.query.first():
        db.session.add(Branch(branch_name='Hayward Hub', location='25800 Carlos Bee Blvd, Hayward, CA', manager='Alice Johnson'))
        db.session.add(Branch(branch_name='Oakland Depot', location='1000 Broadway, Oakland, CA', manager='Bob Smith'))
    
    if not Driver.query.first():
        db.session.add(Driver(driver_name='Mike Rodriguez', phone='510-123-4567', vehicle='Van T7-01', available=True))
        db.session.add(Driver(driver_name='Sarah Patel', phone='510-987-6543', vehicle='Truck T7-02', available=True))
    
    if not Courier.query.first():
        # Sample shipments for analytics
        c1 = Courier(cons_no="T7-XYZ789", ship_name="Sriram Kumar", rev_name="Rahul Sharma", 
                     s_add="Hayward, CA", r_add="San Francisco, CA", weight=2.5, p_type="Box", 
                     priority="Express", cost=35.0, est_delivery="Delivered", driver_id=1)
        c2 = Courier(cons_no="T7-ABC123", ship_name="Priya Patel", rev_name="John Lee", 
                     s_add="Hayward, CA", r_add="Oakland, CA", weight=1.8, p_type="Envelope", 
                     priority="Standard", cost=18.0, est_delivery="In Transit", driver_id=2)
        db.session.add(c1)
        db.session.add(c2)
        db.session.add(CourierTrack(cons_no="T7-XYZ789", status="Delivered", current_city="San Francisco"))
        db.session.add(CourierTrack(cons_no="T7-ABC123", status="In Transit", current_city="Oakland Hub"))
    
    db.session.commit()
    print("✅ LOG: System Reset Complete. Rich demo data loaded for analytics.")