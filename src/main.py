import os
import openai
from dotenv import load_dotenv

# evnファイルを読み込む
load_dotenv()

# APIキーの設定
openai.api_key = os.environ['OPENAI_API_KEY']

# チャット情報記録用の変数
messages = []

print('「Ctrl」+「C」で終了できます。')

try:
    while True:
        # 質問の入力
        user_message = input('user : ')
        messages.append({'role': 'user', 'content': user_message})

        # 会話を送信
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            max_tokens=1024,
            messages=messages
        )

        # レスポンスを取得、保存
        assistant_message = response.choices[0].message
        response_role = assistant_message['role']
        response_content = assistant_message['content']
        message = {'role': response_role, 'content': response_content}
        messages.append(message)

        # レスポンスの表示
        print(f'{response_role} : {response_content}')
except KeyboardInterrupt:
    print('\nFinish')
