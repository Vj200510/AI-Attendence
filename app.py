import os
import ctypes
import glob

# Force-load libwebp.so.7 as libwebp.so.6 before dlib loads
# dlib wheel was compiled against libwebp6, Debian Trixie only has libwebp7
_webp_libs = sorted(glob.glob('/usr/lib/x86_64-linux-gnu/libwebp.so.*'))
for _lib in _webp_libs:
    try:
        ctypes.CDLL(_lib)
        break
    except Exception:
        pass

# Create symlink if it doesn't exist
_target = '/usr/lib/x86_64-linux-gnu/libwebp.so.6'
if not os.path.exists(_target) and _webp_libs:
    try:
        os.symlink(_webp_libs[0], _target)
    except Exception:
        pass

import streamlit as st

from src.screens.home_screen import home_screen
from src.screens.teacher_screen import teacher_screen
from src.screens.student_screen import student_screen

from src.components.dialog_auto_enroll import auto_enroll_dialog

def main():
    st.set_page_config(
        page_title='SnapClass - Making Attendance faster using AI',
        page_icon= "https://i.ibb.co/YTYGn5qV/logo.png"
    )
    if 'login_type' not in st.session_state:
        st.session_state['login_type'] = None

    match st.session_state['login_type']:
        case 'teacher':
            teacher_screen()

        case 'student':
            student_screen()
        
        case None:
            home_screen()


    join_code = st.query_params.get('join-code')
    if join_code:
        if st.session_state.login_type != 'student':
            st.session_state.login_type = 'student'
            st.rerun()
        if st.session_state.get('is_logged_in') and st.session_state.get('user_role') == 'student':
            auto_enroll_dialog(join_code)
main()
