import streamlit as st

st.set_page_config(page_title="Myelooman riskiluokitin", layout="centered")

def classify_risk(del17p_pct, tp53_yes, t1416, t414, del1p1q, b2m_norm_crea):
    triggers = []
    if del17p_pct is not None and del17p_pct >= 20:
        triggers.append("17p-deleetio ≥ 20 %")
    if tp53_yes:
        triggers.append("TP53-muutos")
    if t1416 == 2:
        triggers.append("t(14;16) yhdessä del(1p32)/1q+ kanssa")
    if t414 == 2:
        triggers.append("t(4;14) yhdessä del(1p32)/1q+ kanssa")
    if del1p1q == 2:
        triggers.append("del(1p32)/1q+")

    genetic_high = len(triggers) > 0
    overall_high = genetic_high or (b2m_norm_crea == 2)
    return genetic_high, overall_high, triggers

def label_12(v):
    return "2 = Kyllä" if v == 2 else "1 = Ei"

st.title("Myelooman riskiluokitin")
st.caption("Päätöksentukityökalu. Varmista paikallinen ohjeistus ja validointi.")

col1, col2 = st.columns(2)
with col1:
    del17p_pct = st.number_input("17p-deleetion osuus (%)", 0.0, 100.0, step=0.1, format="%.1f")
    tp53_str = st.radio("TP53-muutos", ["Ei", "Kyllä"], horizontal=True)
    t1416 = st.selectbox("t(14;16)", [1,2], format_func=label_12)
with col2:
    t414 = st.selectbox("t(4;14)", [1,2], format_func=label_12)
    del1p1q = st.selectbox("del(1p32)/1q+", [1,2], format_func=label_12)
    b2m_norm_crea = st.selectbox("B2M >5,5 mg/dL ja normaali krea", [1,2], format_func=label_12)

tp53_yes = (tp53_str == "Kyllä")

if st.button("Laske riski", type="primary"):
    genetic_high, overall_high, triggers = classify_risk(
        del17p_pct, tp53_yes, t1416, t414, del1p1q, b2m_norm_crea
    )
    if overall_high:
        st.error("**Kokonaisriski: KORKEA**")
    else:
        st.success("**Kokonaisriski: STANDARDRISKI**")
    st.divider()
    st.subheader("Perustelut")
    st.markdown(f"- **Geneettinen riski:** {'Korkea' if genetic_high else 'Ei korkea'}")
    if genetic_high:
        st.markdown("  - Täyttyneet geneettiset kriteerit:")
        for t in triggers:
            st.markdown(f"    - {t}")
    st.markdown(f"- **B2M/krea-yhdistelmä:** {'2 = Kyllä' if b2m_norm_crea == 2 else '1 = Ei'}")
