from user import User
from post import Post
# The lesson here is to create objects by 'calling' constructors and giving them values for
# the attributes that we had defined earlier.
app_user_one = User("442.com@nelly", "Nelson Otieno", "number21", "Box2Box Midfielder")
app_user_one.get_user_info()

app_user_two = User("442.com@sancho", "Jadon Sancho", "suuwhoop", "Ball Carrier")
app_user_two.get_user_info()

new_post = Post(" Gunning for the TITLE ", app_user_two.name)
new_post.get_post_info()
