import os
from datetime import date

import requests
import streamlit as st

API_URL = os.getenv("API_URL", "http://localhost:8000")


def calculator_ui() -> None:
    st.header("計算機")
    num1 = st.number_input("輸入第一個數字", value=0.0)
    op = st.selectbox("選擇運算", ["+", "-", "*", "/"])
    num2 = st.number_input("輸入第二個數字", value=0.0)
    if st.button("計算"):
        resp = requests.post(f"{API_URL}/calculator", json={"num1": num1, "op": op, "num2": num2})
        if resp.status_code == 200:
            st.success(f"結果: {resp.json()['result']}")
        else:
            st.error(resp.json().get("detail", "計算錯誤"))


def unit_converter_ui() -> None:
    st.header("單位轉換器")
    unit_type = st.selectbox("選擇單位類型", ["長度", "重量", "溫度"])
    if unit_type == "長度":
        value = st.number_input("輸入長度（公尺）", value=0.0)
        resp = requests.post(f"{API_URL}/convert/length", json={"meters": value})
    elif unit_type == "重量":
        value = st.number_input("輸入重量（公斤）", value=0.0)
        resp = requests.post(f"{API_URL}/convert/weight", json={"kg": value})
    else:
        value = st.number_input("輸入溫度（攝氏）", value=0.0)
        resp = requests.post(f"{API_URL}/convert/temperature", json={"celsius": value})
    if resp.status_code == 200:
        for k, v in resp.json().items():
            st.write(f"{k}: {v}")
    else:
        st.error("轉換失敗")


def bmi_calculator_ui() -> None:
    st.header("BMI 計算器")
    height = st.number_input("身高（公分）", value=170.0)
    weight = st.number_input("體重（公斤）", value=60.0)
    if st.button("計算 BMI"):
        resp = requests.post(
            f"{API_URL}/bmi", json={"height_cm": height, "weight_kg": weight}
        )
        if resp.status_code == 200:
            st.success(f"BMI: {resp.json()['bmi']:.2f}")
        else:
            st.error(resp.json().get("detail", "計算錯誤"))


def date_difference_ui() -> None:
    st.header("日期差距計算器")
    date1 = st.date_input("選擇第一個日期", value=date.today())
    date2 = st.date_input("選擇第二個日期", value=date.today())
    if st.button("計算差距"):
        resp = requests.post(
            f"{API_URL}/date-diff", json={"date1": str(date1), "date2": str(date2)}
        )
        if resp.status_code == 200:
            st.success(f"兩日期相差 {resp.json()['days']} 天")
        else:
            st.error("計算錯誤")


def main() -> None:
    st.title("工具百寶箱")
    tool_functions = {
        "計算機": calculator_ui,
        "單位轉換器": unit_converter_ui,
        "BMI 計算器": bmi_calculator_ui,
        "日期差距計算器": date_difference_ui,
    }
    tool = st.sidebar.selectbox("選擇工具", list(tool_functions.keys()))
    func = tool_functions.get(tool)
    if func:
        func()


if __name__ == "__main__":
    main()
