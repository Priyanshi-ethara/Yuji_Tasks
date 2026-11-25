# EFS region mapping for Talvik sites (data steward note, 2026-05-11)

- Each site's EFS region is fixed in the site register (`efs_region`). US sites map to the EFS US subregion of the
  balancing area that serves the site's supplier; EU and GB sites map to the country.
- Purchased chilled water and steam take the region of the plant that produces them. Capitol Campus Central Plant
  (Albany) sits in US-NE1; Legacy District Cooling (Plano) sits in US-TX4; both are the region of the site they serve.
- US-TX4 covers Waco, Tyler and Plano. US-SE3 covers Greer, Macon and Huntsville. There is no Talvik site in US-CA6,
  US-FL7 or US-AZ8; those rows exist in the EFS for the sales offices' Scope 3 work.
- Gdańsk and Wrocław are both PL even though they have different suppliers.
