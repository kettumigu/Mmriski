
import streamlit as st

def arvioi_riski():
    st.title("Multippeli myelooman riskiluokitus (portaittain)")

    korkea_riski = False

    deleetio_17p = st.number_input("Kuinka suuressa osassa soluja todetaan 17p deleetio? (0-100)", min_value=0, max_value=100, step=1)
    if deleetio_17p >= 20:
        korkea_riski = True
        st.warning("Korkea riskiKORKEA, mPFS 8.4-23.9 kk, mOS 31.2-45.6 kk, perustuen GEM-tutkimuksiin: 17p deleetio ≥ 20%")

    if not korkea_riski:
        tp53 = st.radio("Onko potilaalla TP53-mutaatio/deleetio?", ["ei", "kyllä"])
        if tp53 == "kyllä":
            korkea_riski = True
            st.warning("Korkea riski: TP53-muutos")

    if not korkea_riski:
        t_1416 = st.radio("Onko potilaalla t(14;16)?", ["1 = Ei tai ainoana muutoksena", "2 = Kyllä del(1p32)/1q+ kanssa"])
        if t_1416.startswith("2"):
            korkea_riski = True
            st.warning("Korkea riski: t(14;16) + del(1p32)/1q+")

    if not korkea_riski:
        t_4414 = st.radio("Onko potilaalla t(4;14)?", ["1 = Ei tai ainoana muutoksena", "2 = Kyllä del(1p32)/1q+ kanssa"])
        if t_4414.startswith("2"):
            korkea_riski = True
            st.warning("Korkea riski: t(4;14) + del(1p32)/1q+")

    if not korkea_riski:
        del_1p32_1q = st.radio("Onko bialleelinen del(1p32) tai del(1p32) ja 1q+?", ["1 = Ei", "2 = Kyllä"])
        if del_1p32_1q.startswith("2"):
            korkea_riski = True
            st.warning("Korkea riski: bialleelinen del(1p32) tai del(1p32) ja 1q+")

    if not korkea_riski:
        b2m_krea = st.radio("Onko B2M >5,5 mg/dL ja samanaikaisesti normaali krea?", ["1 = Ei", "2 = Kyllä"])
        if b2m_krea.startswith("2"):
            korkea_riski = True
            st.warning("Korkea riski: B2M/krea-yhdistelmä")

    if korkea_riski:
        st.success("➡️ Riskiluokka: KORKEA")
    else:
        st.info("➡️ Riskiluokka: MATALA")

if __name__ == "__main__":
    arvioi_riski()
