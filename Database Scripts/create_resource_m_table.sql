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
-- Name: resourceManagement; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."resourceManagement" (
    id integer NOT NULL,
    "projectName" character varying NOT NULL,
    duration integer NOT NULL,
    "resourceName" character varying NOT NULL,
    status character varying,
    "updatedDate" timestamp without time zone
);


ALTER TABLE public."resourceManagement" OWNER TO postgres;  

--
-- Name: resourceManagement_id_seq; Type: SEQUENCE; Schema: 
public; Owner: postgres
--

CREATE SEQUENCE public."resourceManagement_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."resourceManagement_id_seq" OWNER TO postgres;

--
-- Name: resourceManagement_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."resourceManagement_id_seq" OWNED BY public."resourceManagement".id;


--
-- Name: resourceManagement id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."resourceManagement" ALTER COLUMN id SET DEFAULT nextval('public."resourceManagement_id_seq"'::regclass);


--
-- Name: resourceManagement resourceManagement_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."resourceManagement"
    ADD CONSTRAINT "resourceManagement_pkey" PRIMARY KEY (id);