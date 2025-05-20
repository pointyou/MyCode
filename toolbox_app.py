import streamlit as st
from datetime import date

st.title("工具百寶箱")

tool = st.sidebar.selectbox(
    "選擇工具",
    ("計算機", "單位轉換器", "BMI 計算器", "日期差距計算器")
)

if tool == "計算機":
    st.header("計算機")
    num1 = st.number_input("輸入第一個數字", value=0.0)
    op = st.selectbox("選擇運算", ["+", "-", "*", "/"])
    num2 = st.number_input("輸入第二個數字", value=0.0)
    if st.button("計算"):
        if op == "+":
            st.success(f"結果: {num1 + num2}")
        elif op == "-":
            st.success(f"結果: {num1 - num2}")
        elif op == "*":
            st.success(f"結果: {num1 * num2}")
        elif op == "/":
            if num2 != 0:
                st.success(f"結果: {num1 / num2}")
            else:
                st.error("除數不能為零")

elif tool == "單位轉換器":
    st.header("單位轉換器")
    unit_type = st.selectbox("選擇單位類型", ["長度", "重量", "溫度"])
    if unit_type == "長度":
        length = st.number_input("輸入長度（公尺）", value=0.0)
        st.write(f"公尺: {length}")
        st.write(f"公分: {length * 100}")
        st.write(f"公里: {length / 1000}")
        st.write(f"英吋: {length * 39.3701}")
        st.write(f"英呎: {length * 3.28084}")
    elif unit_type == "重量":
        weight = st.number_input("輸入重量（公斤）", value=0.0)
        st.write(f"公斤: {weight}")
        st.write(f"公克: {weight * 1000}")
        st.write(f"磅: {weight * 2.20462}")
        st.write(f"盎司: {weight * 35.274}")
    elif unit_type == "溫度":
        c = st.number_input("輸入溫度（攝氏）", value=0.0)
        st.write(f"攝氏: {c}")
        st.write(f"華氏: {c * 9/5 + 32}")
        st.write(f"開爾文: {c + 273.15}")

elif tool == "BMI 計算器":
    st.header("BMI 計算器")
    height = st.number_input("身高（公分）", value=170.0)
    weight = st.number_input("體重（公斤）", value=60.0)
    if st.button("計算 BMI"):
        if height > 0:
            bmi = weight / ((height / 100) ** 2)
            st.success(f"BMI: {bmi:.2f}")
        else:
            st.error("身高需大於 0")

elif tool == "日期差距計算器":
    st.header("日期差距計算器")
    date1 = st.date_input("選擇第一個日期", value=date.today())
    date2 = st.date_input("選擇第二個日期", value=date.today())
    if st.button("計算差距"):
        diff = abs((date2 - date1).days)
        st.success(f"兩日期相差 {diff} 天")
