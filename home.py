from zlai.llms import Zhipu
from zlai.llms.generate_config.api import GLM4GenerateConfig, GLM4FlashGenerateConfig
import streamlit as st
from prompt import choice_prompt


page_name = "公考出题"
st.set_page_config(
    page_title=page_name,
    page_icon=":robot:",
    layout='centered',
    initial_sidebar_state='expanded',
)
st.header(f":blue[{page_name}]", divider='rainbow')


def init_page_cache():
    """"""
    if st.session_state.get('PAGE_NAME') != page_name:
        st.session_state['PAGE_NAME'] = page_name


def main():
    """"""
    file_uploader = st.file_uploader("请上传材料文件", type=['md', 'txt'], )
    submit = st.button("提交", type="primary")
    llm = Zhipu(generate_config=GLM4GenerateConfig(stream=True))

    if file_uploader and submit:
        with st.spinner("正在处理中..."):
            content = file_uploader.getvalue().decode('utf-8')
            messages = [choice_prompt.format_prompt(content=content).to_messages(role="user")]
            completion = llm.generate(messages=messages)
            placeholder = st.empty()
            answer = ""
            for chunk in completion:
                answer += chunk.choices[0].delta.content
                placeholder.markdown(answer)
    else:
        st.warning("请上传PPT文件")


if __name__ == "__main__":
    main()
