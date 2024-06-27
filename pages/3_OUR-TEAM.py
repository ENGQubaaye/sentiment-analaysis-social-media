# import streamlit as st
# from PIL import Image, ImageOps

# # Load the icon image for the page
# icon = Image.open('./1.png')  # Provide the path to your icon image

# # Configure Streamlit page settings
# st.set_page_config(
#     page_title='OUR-TEAM',  # Title of the page
#     page_icon=icon,  # Icon for the page
#     layout='wide',  # Page layout (wide)
#     initial_sidebar_state='auto',  # Initial sidebar state (auto, collapsed, expanded)
#     menu_items={
#         'Get Help': 'https://streamlit.io',  # Help menu item with link
#         'Report a bug': 'https://github.com',  # Report a bug menu item with link
#         'About': 'About your application: *Hello World!*'  # About menu item with description
#     }
# )

# # Define CSS styles for background image, header, and image borders
# page_bg_img = f"""
# # <style>
# # [data-testid="stAppViewContainer"] > .main {{
# #     background-size: 140%;
# #     background-position: top left;
# #     background-repeat: no-repeat;
# #     background-attachment: local;
# #     primaryColor="#d8e00e"
# #     backgroundColor="#1e64b7"
# #     secondaryBackgroundColor="#1d1d1e"
# #     textColor="#fdfdfd"
# # }}

# # [data-testid="stHeader"] {{
# #     background: rgba(0,0,0,0);
# # }}
# # [data-testid="stToolbar"] {{
# #     right: 2rem;
# # }}
# # img {{
# #     border-radius: 15px;  /* Adjust the value to your preference */
# # }}
# # .team-member {{
# #     border-radius: 15px;
# #     padding: 10px;
# #     margin: 10px 0;
# # }}
# # .social-icons img {{
# #     width: 100px;
# #     height: 10s0px;
# #     margin-right: 5px;
# # }}
# # </style>
# # """

# # # Hide Streamlit's default styles
# # hide_st_style = """
# # <style>
# # #MainMenu {visibility: hidden;}
# # footer {visibility: hidden;}
# # header {visibility: hidden;}
# # </style>
# # """
# # st.markdown(hide_st_style, unsafe_allow_html=True)

# # # Apply the background image and header styles
# # st.markdown(page_bg_img, unsafe_allow_html=True)

# # # Create an option menu using the custom 'option_menu' function


# # # Define a function to preprocess and display images with the same size and border radius
# # def display_member_info(name, picture_path, facebook_url, instagram_url):
# #     st.markdown(f"<div class='team-member'>", unsafe_allow_html=True)
# #     st.write(f"**Name:** {name}")
# #     image = Image.open(picture_path)
# #     image = ImageOps.fit(image, (100, 100))  # Ensure all images are 100x100 pixels
# #     st.image(image, use_column_width=True)

# #     st.write("**Social Media Links:**")
    
# #     social_media_icons = {
# #         "Facebook": "https://upload.wikimedia.org/wikipedia/commons/5/51/Facebook_f_logo_%282019%29.svg",
# #         "Instagram": "https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png",
# #     }
    
# #     st.markdown(f"""
# #     <div class='social-icons'>
# #         <a href="{facebook_url}" target="_blank"><img src="{social_media_icons['Facebook']}" alt="Facebook"></a>
# #         <a href="{instagram_url}" target="_blank"><img src="{social_media_icons['Instagram']}" alt="Instagram"></a>
# #     </div>
# #     """, unsafe_allow_html=True)

# #     st.markdown("</div>", unsafe_allow_html=True)
# #     st.write("---")  # Add a separator between members

# # team_members = [
# #     {
# #         "name": "Abdulaahi hassan Adam",
# #         "picture_path": "Abdulahi.PNG",
# #         "facebook_url": "https://www.facebook.com/profile.php?id=100052766480581&mibextid=ZbWKwL",
# #         "instagram_url": "https://www.instagram.com/ainab",
        
# #     },
# #     {
# #         "name": " AbdiNasir mohamed isackh ",
# #         "picture_path": "cade.jpg",
# #         "facebook_url": "https://www.facebook.com/abdinaasir.qubaaye?mibextid=ZbWKwL",
# #         "instagram_url": "https://www.instagram.com/johndoe",
        
# #     },
# #     {
# #         "name": "mohamed amiin Abdirizaaq",
# #         "picture_path": "cade1.jpg",
# #         "facebook_url":"https://www.facebook.com/sarahlee",
# #         "instagram_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/58/Instagram-Icon.png/1200px-Instagram-Icon.png",
# #     },
# #     {
# #         "name": "Abdullahi",
# #         "picture_path": "ainab.jpg",
# #         "facebook_url": "https://www.facebook.com/sarahlee",
# #         "instagram_url": "https://www.instagram.com/johndoe",
# #     },
    
# # ]

# import streamlit as st
# from PIL import Image, ImageOps

# # Define CSS styles for background image, header, and image borders
# page_bg_img = f"""
# <style>
# [data-testid="stAppViewContainer"] > .main {{
#     background-size: 140%;
#     background-position: top left;
#     background-repeat: no-repeat;
#     background-attachment: local;
#     primaryColor="#d8e00e";
#     backgroundColor="#1e64b7";
#     secondaryBackgroundColor="#1d1d1e";
#     textColor="#fdfdfd";
# }}

# [data-testid="stHeader"] {{
#     background: rgba(0,0,0,0);
# }}
# [data-testid="stToolbar"] {{
#     right: 2rem;
# }}
# img {{
#     border-radius: 50%;  /* Circular images */
# }}
# .team-member {{
#     border-radius: 15px;
#     padding: 10px;
#     margin: 10px 0;
# }}
# .social-icons img {{
#     width: 30px;  /* Smaller icons */
#     height: 30px;
#     margin-right: 5px;
# }}
# </style>
# """

# # Hide Streamlit's default styles
# hide_st_style = """
# <style>
# #MainMenu {visibility: hidden;}
# footer {visibility: hidden;}
# header {visibility: hidden;}
# </style>
# """
# st.markdown(hide_st_style, unsafe_allow_html=True)

# # Apply the background image and header styles
# st.markdown(page_bg_img, unsafe_allow_html=True)

# # Define a function to preprocess and display images with the same size and border radius
# def display_member_info(name, picture_path, facebook_url, instagram_url):
#     st.markdown(f"<div class='team-member'>", unsafe_allow_html=True)
#     st.write(f"**Name:** {name}")
#     image = Image.open(picture_path)
#     image = ImageOps.fit(image, (100, 100))  # Ensure all images are 100x100 pixels
#     st.image(image, use_column_width=False)  # Set use_column_width to False for fixed size

#     st.write("**Social Media Links:**")
    
#     social_media_icons = {
#         "Facebook": "https://upload.wikimedia.org/wikipedia/commons/5/51/Facebook_f_logo_%282019%29.svg",
#         "Instagram": "https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png",
#     }
    
#     st.markdown(f"""
#     <div class='social-icons'>
#         <a href="{facebook_url}" target="_blank"><img src="{social_media_icons['Facebook']}" alt="Facebook"></a>
#         <a href="{instagram_url}" target="_blank"><img src="{social_media_icons['Instagram']}" alt="Instagram"></a>
#     </div>
#     """, unsafe_allow_html=True)

#     st.markdown("</div>", unsafe_allow_html=True)
#     st.write("---")  # Add a separator between members

# # Example usage
# team_members = [
#     {
#         "name": "Abdulaahi hassan Adam",
#         "picture_path": "Abdulahi.PNG",
#         "facebook_url": "https://www.facebook.com/profile.php?id=100052766480581&mibextid=ZbWKwL",
#         "instagram_url": "https://www.instagram.com/ainab",
#     },
#     {
#         "name": "AbdiNasir mohamed isackh",
#         "picture_path": "cade.jpg",
#         "facebook_url": "https://www.facebook.com/abdinaasir.qubaaye?mibextid=ZbWKwL",
#         "instagram_url": "https://www.instagram.com/johndoe",
#     },
#     {
#         "name": "mohamed amiin Abdirizaaq",
#         "picture_path": "cade1.jpg",
#         "facebook_url": "https://www.facebook.com/sarahlee",
#         "instagram_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/58/Instagram-Icon.png/1200px-Instagram-Icon.png",
#     },
#     {
#         "name": "Abdullahi",
#         "picture_path": "ainab.jpg",
#         "facebook_url": "https://www.facebook.com/sarahlee",
#         "instagram_url": "https://www.instagram.com/johndoe",
#     },
# ]

# for member in team_members:
#     display_member_info(
#         name=member["name"],
#         picture_path=member["picture_path"],
#         facebook_url=member["facebook_url"],
#         instagram_url=member["instagram_url"]
#     )

# import streamlit as st
# from PIL import Image, ImageOps

# # Define CSS styles for background image, header, and image borders
# page_bg_img = f"""
# <style>
# [data-testid="stAppViewContainer"] > .main {{
#     background-size: 140%;
#     background-position: top left;
#     background-repeat: no-repeat;
#     background-attachment: local;
#     primaryColor="#d8e00e";
#     backgroundColor="#1e64b7";
#     secondaryBackgroundColor="#1d1d1e";
#     textColor="#fdfdfd";
# }}

# [data-testid="stHeader"] {{
#     background: rgba(0,0,0,0);
# }}
# [data-testid="stToolbar"] {{
#     right: 2rem;
# }}
# img {{
#     border-radius: 50%;  /* Circular images */
# }}
# .team-member {{
#     border-radius: 15px;
#     padding: 10px;
#     margin: 10px 0;
# }}
# .social-icons img {{
#     width: 30px;  /* Smaller icons */
#     height: 30px;
#     margin-right: 5px;
# }}
# </style>
# """

# # Hide Streamlit's default styles
# hide_st_style = """
# <style>
# #MainMenu {visibility: hidden;}
# footer {visibility: hidden;}
# header {visibility: hidden;}
# </style>
# """
# st.markdown(hide_st_style, unsafe_allow_html=True)

# # Apply the background image and header styles
# st.markdown(page_bg_img, unsafe_allow_html=True)

# # Define a function to preprocess and display images with the same size and border radius
# def display_member_info(name, picture_path, facebook_url, instagram_url):
#     st.markdown(f"<div class='team-member'>", unsafe_allow_html=True)
#     st.write(f"**Name:** {name}")
#     image = Image.open(picture_path)
#     image = ImageOps.fit(image, (50, 50))  # Ensure all images are 50x50 pixels
#     st.image(image, use_column_width=False)  # Set use_column_width to False for fixed size

#     st.write("**Social Media Links:**")
    
#     social_media_icons = {
#         "Facebook": "https://upload.wikimedia.org/wikipedia/commons/5/51/Facebook_f_logo_%282019%29.svg",
#         "Instagram": "https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png",
#     }
    
#     st.markdown(f"""
#     <div class='social-icons'>
#         <a href="{facebook_url}" target="_blank"><img src="{social_media_icons['Facebook']}" alt="Facebook"></a>
#         <a href="{instagram_url}" target="_blank"><img src="{social_media_icons['Instagram']}" alt="Instagram"></a>
#     </div>
#     """, unsafe_allow_html=True)

#     st.markdown("</div>", unsafe_allow_html=True)
#     st.write("---")  # Add a separator between members

# # Example usage


# for member in team_members:
#     display_member_info(
#         name=member["name"],
#         picture_path=member["picture_path"],
#         facebook_url=member["facebook_url"],
#         instagram_url=member["instagram_url"]
#     )


# col1, col2 = st.columns(2)

# for i, member in enumerate(team_members):
#     if i % 2 == 0:
#         with col1:
#             display_member_info(
#                 member["name"],
#                 member["picture_path"],
#                 member["facebook_url"],
#                 member["instagram_url"]
                
#             )
#     else:
#         with col2:
#             display_member_info(
#                 member["name"],
#                 member["picture_path"],
#                 member["facebook_url"],
#                 member["instagram_url"]
               
#             )


import streamlit as st
from PIL import Image, ImageOps

# Load the icon image for the page
icon = Image.open('./1.png')  # Provide the path to your icon image

# Configure Streamlit page settings
st.set_page_config(
    page_title='OUR-TEAM',  # Title of the page
    page_icon=icon,  # Icon for the page
    layout='wide',  # Page layout (wide)
    initial_sidebar_state='auto',  # Initial sidebar state (auto, collapsed, expanded)
    menu_items={
        'Get Help': 'https://streamlit.io',  # Help menu item with link
        'Report a bug': 'https://github.com',  # Report a bug menu item with link
        'About': 'About your application: *Hello World!*'  # About menu item with description
    }
)

# Define CSS styles for background image, header, and image borders
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
    background-size: 140%;
    background-position: top left;
    background-repeat: no-repeat;
    background-attachment: local;
    primaryColor="#d8e00e";
    backgroundColor="#1e64b7";
    secondaryBackgroundColor="#1d1d1e";
    textColor="#fdfdfd";
}}

[data-testid="stHeader"] {{
    background: rgba(0,0,0,0);
}}
[data-testid="stToolbar"] {{
    right: 2rem;
}}
img {{
    border-radius: 50%;  /* Circular images */
}}
.team-member {{
    border-radius: 15px;
    padding: 10px;
    margin: 10px 0;
}}
.social-icons img {{
    width: 30px;  /* Smaller icons */
    height: 30px;
    margin-right: 5px;
}}
</style>
"""

# Hide Streamlit's default styles
hide_st_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

# Apply the background image and header styles
st.markdown(page_bg_img, unsafe_allow_html=True)

# Define a function to preprocess and display images with the same size and border radius
def display_member_info(name, picture_path, facebook_url, instagram_url):
    st.markdown(f"<div class='team-member'>", unsafe_allow_html=True)
    st.write(f"**Name:** {name}")
    image = Image.open(picture_path)
    image = ImageOps.fit(image, (150, 150))  # Ensure all images are 150x150 pixels
    st.image(image, use_column_width=False)  # Set use_column_width to False for fixed size

    st.write("**Social Media Links:**")
    
    social_media_icons = {
        "Facebook": "https://upload.wikimedia.org/wikipedia/commons/5/51/Facebook_f_logo_%282019%29.svg",
        "Instagram": "https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png",
    }
    
    st.markdown(f"""
    <div class='social-icons'>
        <a href="{facebook_url}" target="_blank"><img src="{social_media_icons['Facebook']}" alt="Facebook"></a>
        <a href="{instagram_url}" target="_blank"><img src="{social_media_icons['Instagram']}" alt="Instagram"></a>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
    st.write("---")  # Add a separator between members

# Example usage
team_members = [
    {
        "name": "Abdulaahi hassan Adam",
        "picture_path": "Abdulahi.PNG",
        "facebook_url": "https://www.facebook.com/profile.php?id=100052766480581&mibextid=ZbWKwL",
        "instagram_url": "https://www.instagram.com/ainab",
    },
    {
        "name": "AbdiNasir mohamed isackh",
        "picture_path": "Nasir.png",
        "facebook_url": "https://www.facebook.com/abdinaasir.qubaaye?mibextid=ZbWKwL",
        "instagram_url": "https://www.instagram.com/johndoe",
    },
    {
        "name": "mohamed amiin Abdirizaaq",
        "picture_path": "cade1.jpg",
        "facebook_url": "https://www.facebook.com/sarahlee",
        "instagram_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/58/Instagram-Icon.png/1200px-Instagram-Icon.png",
    },
    {
        "name": "Jamac  adan dimcad",
        "picture_path": "jamac.png",
        "facebook_url": "https://www.facebook.com/hanadaadan.dimcad?mibextid=LQQJ4d",
        "instagram_url": "https://www.instagram.com/johndoe",
    },
]

# Display team members in two columns
col1, col2 = st.columns(2)

for i, member in enumerate(team_members):
    if i % 2 == 0:
        with col1:
            display_member_info(
                member["name"],
                member["picture_path"],
                member["facebook_url"],
                member["instagram_url"]
            )
    else:
        with col2:
            display_member_info(
                member["name"],
                member["picture_path"],
                member["facebook_url"],
                member["instagram_url"]
            )
