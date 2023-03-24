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
        self.activity_name = activity['activity_name']
        self.duration = activity['duration']
        self.description = activity['description']
        self.created_at = activity['created_at']
        self.updated_at = activity['updated_at']
        self.user = user.User.get_by_id(activity["user_id"])

    @classmethod
    def get_all(cls):
        query = """SELECT activities.id, activities.activity_name, activities.genre, activities.city, activities.created_at, activities.updated_at,
            users.id as user_id, first_name, last_name, email, users.created_at as uc, users.updated_at as uu
            FROM activities
            JOIN users on users.id = activities.user_id;"""
        activity_data = connectToMySQL('planner_schema').query_db(query)
        activities = []
        for activity in activity_data:
            activity_obj = cls(activity)
            activity_obj.user = user.User(
                {
                    "id":activity["user_id"],
                    "first_name":activity["first_name"],
                    "last_name":activity["last_name"],
                    "email":activity["email"],
                    "created_at":activity["uc"],
                    "updated_at":activity["uu"]
                }
            )
            activities.append (activity_obj)
        return activities

    @classmethod
    def get_by_id(cls,activity_id):
        data = {"id": activity_id}
        query = """SELECT activities.id, activities.activity_name, activities.genre, activities.city, activities.created_at, activities.updated_at,
		users.id AS user_id, users.first_name AS first_name, users.last_name AS last_name, users.email AS email, users.created_at AS uc, users.updated_at AS uu
            FROM activities 
            JOIN users ON users.id = activities.user_id 
            WHERE activities.id = %(id)s; """
        result = connectToMySQL('planner_schema').query_db(query,data)
        print("result of query")
        print(result)
        result=result[0]
        activity=cls(result)
        activity.user = user.User(
                        {
                    "id":result["user_id"],
                    "first_name":result["first_name"],
                    "last_name":result["last_name"],
                    "email":result["email"],
                    "created_at":result["uc"],
                    "updated_at":result["uu"]
                }
            )
        return activity
    
    @classmethod
    def get_all_by_user(cls,user_id):
        data = {
            "user_id" : user_id
        }
        query = """SELECT activities.id, activities.activity_name, activities.genre, activities.city, activities.created_at, activities.updated_at,
            users.id as user_id, first_name, last_name, email, users.created_at as uc, users.updated_at as uu
            FROM activities
            JOIN users on users.id = activities.user_id
            WHERE users.id = %(user_id)s;"""
        activity_data = connectToMySQL('planner_schema').query_db(query, data)
        activities = []
        for activity in activity_data:
            activity_obj = cls(activity)
            activity_obj.user = user.User(
                {
                    "id":activity["user_id"],
                    "first_name":activity["first_name"],
                    "last_name":activity["last_name"],
                    "email":activity["email"],
                    "created_at":activity["uc"],
                    "updated_at":activity["uu"]
                }
            )
            activities.append (activity_obj)
        return activities

    @classmethod
    def create_valid_activity(cls, activity):
        is_valid = True
        if len(activity["name"]) < 3:
            flash("Activity must be at least 3 characters","create")
            is_valid=False
        if len(activity['description']) < 3:
            flash("Description must be at least 6 characters","create")
            is_valid= False
        if len(activity['duration']) < 3:
            flash("Duration must be a numerical value","create")
            is_valid= False
        if is_valid:
            return None
        else:
            return None
        
    @classmethod #  UPDATE Activity
    def update_activity(cls, activity_dict, session_id):
        activity = cls.get_by_id(activity_dict["id"])
        if activity.user.id != session_id:
            flash("You are not the founding member!")
            return False
        if not cls.is_valid(activity_dict):
            return False
        
        query = """UPDATE activities SET activity_name = %(activity_name)s, duration = %(duration)s, description = %(description)s
            WHERE id = %(id)s;"""
        result = connectToMySQL('activity_together_schema').query_db(query,activity_dict)
        activity = cls.get_by_id(activity_dict["id"])
        return activity