-- This is for a postgres database

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
-- Name: capability; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.capability (
    id integer NOT NULL,
    number integer NOT NULL,
    name character varying NOT NULL,
    size character varying NOT NULL,
    status character varying NOT NULL,
    length integer NOT NULL,
    dependency character varying DEFAULT 'N/A'::character varying NOT NULL
);


ALTER TABLE public.capability OWNER TO postgres;

--
-- Name: capability_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.capability_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.capability_id_seq OWNER TO postgres;

--
-- Name: capability_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.capability_id_seq OWNED BY public.capability.id;


--
-- Name: capability id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.capability ALTER COLUMN id SET DEFAULT nextval('public.capability_id_seq'::regclass);


--
-- Name: capability capability_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.capability
    ADD CONSTRAINT capability_pkey PRIMARY KEY (id);
