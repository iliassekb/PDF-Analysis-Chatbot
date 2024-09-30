css = '''
<style>
   

        .chat-message {
            display: flex;
            align-items: flex-start;
            margin-bottom: 1rem;
        }

        .chat-message.user {
            justify-content: flex-end;
        }

        .chat-message.bot {
            justify-content: flex-start;
        }

        .chat-message .avatar {
            width: 50px;
            height: 50px;
            border-radius: 50%;
            overflow: hidden;
            margin: 0 1rem;
            flex-shrink: 0;
        }

        .chat-message .avatar img {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }

        .chat-message .message {
            max-width: 75%;
            padding: 0.75rem 1rem;
            border-radius: 20px;
            position: relative;
            font-size: 1rem;
            line-height: 1.5;
        }

        .chat-message.user .message {
            background-color: #2b313e;
            color: #fff;
            border-top-right-radius: 0;
        }

        .chat-message.bot .message {
            background-color: #475063;
            color: #fff;
            border-top-left-radius: 0;
        }
    </style>

'''

bot_template = '''
 <div class="chat-message bot">
            <div class="avatar">
                <img src="https://i.pinimg.com/736x/fd/a1/3b/fda13b9d6d88f25a9d968901d319216a.jpg" alt="Bot Avatar">
            </div>
            <div class="message">{{MSG}}</div>
        </div>
'''

user_template = '''
<div class="chat-message user">
            <div class="avatar">
                <img src="https://static.vecteezy.com/system/resources/previews/002/318/271/original/user-profile-icon-free-vector.jpg" alt="Bot Avatar">
            </div>
            <div class="message">{{MSG}}</div>
        </div>
'''