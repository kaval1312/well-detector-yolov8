import streamlit as st
import PIL

st.set_page_config(
    page_title="Well detection using YOLOv8",  # Setting page title
    page_icon="🛢",     # Setting page icon
    layout="wide",      # Setting layout to wide
    initial_sidebar_state="expanded"    # Expanding sidebar by default
)

st.title("Приложение для обнаружения нефтяных скважин")

st.markdown(
"""
В эпоху, когда нефть и газ остаются ключевыми ресурсами для экономики и жизни населения,
эффективное управление нефтегазовыми запасами играет важнейшую роль.
Это особенно актуально в контексте глобальных вызовов, связанных с энергосбережением и сокращением углеродных выбросов.
 Нефтяные скважины, как основные источники добычи, являются важными индикаторами в этой сфере.
Их мониторинг с помощью спутниковых снимков позволяет оценить глобальные тенденции в нефтедобыче и управлении ресурсами.  

Данное приложение, разработанное на базе YOLOv8, предназначено для детекции нефтяных скважин на спутниковых снимках, используя данные из двух исследований.
"""
)

link1 =  '[Oil Well Detection under Occlusion in Remote Sensing Images Using the Improved YOLOv5 Model, 2023](https://www.mdpi.com/2072-4292/15/24/5788#)' 
link2 = '[An Oil Well Dataset Derived from Satellite-Based Remote Sensing, 2021](https://www.mdpi.com/2072-4292/13/6/1132)'
st.markdown(link1, unsafe_allow_html=True)
st.markdown(link2, unsafe_allow_html=True)
st.title("Как использовать приложение:")
st.markdown(
"""
1) **Открытие**: В боковом меню выберите вкладку "Detect".  
2) **Загрузка изображения**: Загрузите свой спутниковый снимок для детекции скважин или выберите из предзагруженных образцов.  
3) **Обнаружение**: Нажмите на "Detect Objects" в боковом меню для запуска анализа.  
4) **Настройка**: Если результаты не удовлетворяют, измените настройки модели (порог уверенности, IOU) и повторите обнаружение.   
Вы восхитительны!
"""
)
