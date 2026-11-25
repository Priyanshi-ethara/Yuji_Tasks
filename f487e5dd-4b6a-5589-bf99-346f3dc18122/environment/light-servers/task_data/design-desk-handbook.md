# Design desk handbook (extract, revised October 2026)

## 1. What the desk does
The desk reviews every residential string design before it is released to installation. A review ends with a verdict under the string sizing standard in force, the design's maximum string Voc and the string length to build. Sales owns the deal pipeline: the desk never moves a deal between stages and never touches the amount. Customers hear about their design from their sales contact; the desk does not write to customers.

## 2. Where things live
| What | Where |
|---|---|
| The standard (DS-6) | Confluence, Design Engineering space |
| Weekly design register | shared folder (data export) |
| Site surveys | Dropbox › Design Desk › <week> › Site surveys |
| Module datasheets | Box › Engineering › Module datasheets |
| Inverter limits | Notion › Procurement engineering › Inverter catalogue |
| Climate | Airtable base "Site climate list" |
| Review record | HubSpot deal properties; Linear team DESIGN for returns |

## 3. HubSpot properties
- design_status: one DS-6 label, exactly as spelled in the standard.
- max_string_voc: volts, one decimal, the design as submitted.
- modules_per_string: whole number; the length the design is to be built with.
Leave every other property alone.

## 4. Linear
One issue per return in team DESIGN, title `DS6 <deal id> — <verdict>`. The week's project carries the closing summary in its description; the W45 project shows the layout.

## 5. Things that have bitten us
- Module registers and quick-reference sheets drift from the datasheets. They are for first passes only.
- Datasheets do not all use the same units for temperature coefficients.
- The coldest-month mean is not the design minimum any more (Edition 4).
- Two inverter models can share most of a name.
