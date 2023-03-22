from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user
import re

class Activity:
    """Activity function"""
    # db = "planner_schema"
    def __init__(self, activity):
        self.id = activity['id']
        self.activity = activity['activity']
        self.duration = activity['duration']
        self.description = activity['description']
        self.created_at = activity['created_at']
        self.updated_at = activity['updated_at']
        self.user = user.User.get_by_id(activity["user_id"])

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM activities;"
        results = connectToMySQL('planner_schema').query_db(query)
        activities = []
        for row in results:
            activities.append (cls(row))
        return activities

    @classmethod
    def get_by_id(cls,activity_id):
        data = {"id": activity_id}
        query = "SELECT * FROM activities WHERE id = %(id)s;"
        results = connectToMySQL('planner_schema').query_db(query,data)
        return cls(results[0])

    @classmethod
    def create_valid_activity(cls,activity):
        is_valid = True
        if len(activity["activity"]) < 3:
            flash("Activity must be atleast 3 chacters","create")
            is_valid=False
        if len(activity['description']) < 3:
            flash("Description must be at least 6 characters","create")
            is_valid= False
        if len(activity['duration']) < 3:
            flash("Duration must be a a numerical value","create")
            is_valid= False
        if is_valid:
            return None
        else:
            return None