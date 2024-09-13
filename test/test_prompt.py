import unittest
from prompt import choice_prompt
from zlai.llms import Zhipu
from zlai.llms.generate_config.api import GLM4FlashGenerateConfig


content = """
要完善宪法宣传教育工作格局，深化宪法宣誓、宪法纪念、国家象征和标志等制度的教育功能，推动宪法宣传教育常态化长效化。要抓住领导干部这个关键少数，抓住青少年、网民等重点群体，抓宪法纪念、宪法宣誓、宪法教材建设等重点载体，抓学校、社区、媒体等重点阵地，持续深入开展宪法宣传教育。要结合当代中国宪法制度和宪法实践，加强中国宪法理论研究，提炼标志性概念、原创性观点，加强中国宪法学科体系、学术体系、话语体系建设，巩固中国宪法理论在我国法治教育中的指导地位。要讲好中国宪法故事，有自信、有志气宣传中国宪法制度、宪法理论的显著优势和强大生命力，有骨气、有底气同一切歪曲、抹黑、攻击中国宪法的错误言行作斗争。
"""


class TestPrompt(unittest.TestCase):
    """"""

    def test_prompt(self):
        llm = Zhipu(generate_config=GLM4FlashGenerateConfig())
        messages = [choice_prompt.format_prompt(content=content).to_messages(role="user")]
        completion = llm.generate(messages=messages)
        print(completion.choices[0].message.content)
