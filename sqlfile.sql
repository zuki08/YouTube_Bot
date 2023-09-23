--
-- PostgreSQL database dump
--

-- Dumped from database version 15.4
-- Dumped by pg_dump version 15.4

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: info; Type: TABLE; Schema: public; Owner: jeff
--

CREATE TABLE public.info (
    id integer NOT NULL,
    title character varying(255) COLLATE 'zh-CN',
    link character varying(255)
);


ALTER TABLE public.info OWNER TO jeff;

--
-- Data for Name: info; Type: TABLE DATA; Schema: public; Owner: jeff
--

COPY public.info (id, title, link) FROM stdin;
\.


--
-- Name: info info_pkey; Type: CONSTRAINT; Schema: public; Owner: jeff
--

ALTER TABLE ONLY public.info
    ADD CONSTRAINT info_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

