from django.db import models
import uuid

a_l0 = {
            "12": {
              "name": "1 year",
              "loan_roi": 21.8
            },
            "24": {
              "name": "1+ 1 year",
              "loan_roi": 20.9
            },
            "36": {
              "name": "2+1 years",
              "loan_roi": 19.1
            },
            "48": {
              "name": "3+1 years",
              "loan_roi": 17.0
            }
}
a_l1 = {
            "12": {
              "name": "1 year",
              "loan_roi": 23.0
            },
            "24": {
              "name": "1+ 1 year",
              "loan_roi": 22.7
            },
            "36": {
              "name": "2+1 years",
              "loan_roi": 20.8
            },
            "48": {
              "name": "3+1 years",
              "loan_roi":  18.9
            }
}
a_l2 = {
            "12": {
              "name": "1 year",
              "loan_roi": 24.0
            },
            "24": {
              "name": "1+ 1 year",
              "loan_roi": 23.0
            },
            "36": {
              "name": "2+1 years",
              "loan_roi": 21.1
            },
            "48": {
              "name": "3+1 years",
              "loan_roi":  19.3
            }
}
a_l3 = {
            "12": {
              "name": "1 year",
              "loan_roi": 24.2
            },
            "24": {
              "name": "1+ 1 year",
              "loan_roi": 23.4
            },
            "36": {
              "name": "2+1 years",
              "loan_roi": 21.8
            },
            "48": {
              "name": "3+1 years",
              "loan_roi":  20.0
            }
}


b_l0 =  {
            "12": {
              "name": "1 year",
              "loan_roi": 22.8
            },
            "24": {
              "name": "1+ 1 year",
              "loan_roi": 21.9
            },
            "36": {
              "name": "2+1 years",
              "loan_roi": 20.1
            },
            "48": {
              "name": "3+1 years",
              "loan_roi":  18.0
            }
}
				
b_l1 =  {
            "12": {
              "name": "1 year",
              "loan_roi": 24.0
            },
            "24": {
              "name": "1+ 1 year",
              "loan_roi": 23.7
            },
            "36": {
              "name": "2+1 years",
              "loan_roi": 21.8
            },
            "48": {
              "name": "3+1 years",
              "loan_roi": 19.9
            }
}
				
b_l2 =  {
            "12": {
              "name": "1 year",
              "loan_roi": 25.0
            },
            "24": {
              "name": "1+ 1 year",
              "loan_roi": 24.0
            },
            "36": {
              "name": "2+1 years",
              "loan_roi": 22.1
            },
            "48": {
              "name": "3+1 years",
              "loan_roi": 20.3

            }
}
				
b_l3 = {
            "12": {
              "name": "1 year",
              "loan_roi": 25.2
            },
            "24": {
              "name": "1+ 1 year",
              "loan_roi":24.4
            },
            "36": {
              "name": "2+1 years",
              "loan_roi": 22.8
            },
            "48": {
              "name": "3+1 years",
              "loan_roi": 21.0

            }
}
				
c_l0 =  {
            "12": {
              "name": "1 year",
              "loan_roi": 23.8
            },
            "24": {
              "name": "1+ 1 year",
              "loan_roi": 22.9
            },
            "36": {
              "name": "2+1 years",
              "loan_roi": 21.1
            },
            "48": {
              "name": "3+1 years",
              "loan_roi":  19.0
            }
}
							
c_l1 =  {
            "12": {
              "name": "1 year",
              "loan_roi": 23.8
            },
            "24": {
              "name": "1+ 1 year",
              "loan_roi": 22.9
            },
            "36": {
              "name": "2+1 years",
              "loan_roi": 21.1
            },
            "48": {
              "name": "3+1 years",
              "loan_roi": 19.0
            }
}
								
c_l2 =  {
            "12": {
              "name": "1 year",
              "loan_roi": 26.0
            },
            "24": {
              "name": "1+ 1 year",
              "loan_roi": 25.0
            },
            "36": {
              "name": "2+1 years",
              "loan_roi": 23.1
            },
            "48": {
              "name": "3+1 years",
              "loan_roi": 21.3

            }
}
				

c_l3 = {
            "12": {
              "name": "1 year",
              "loan_roi": 26.2
            },
            "24": {
              "name": "1+ 1 year",
              "loan_roi": 25.4
            },
            "36": {
              "name": "2+1 years",
              "loan_roi": 23.8
            },
            "48": {
              "name": "3+1 years",
              "loan_roi": 22.0

            }
}

d_l0 =  {
            "12": {
              "name": "1 year",
              "loan_roi": 24.8
            },
            "24": {
              "name": "1+ 1 year",
              "loan_roi": 23.9
            },
            "36": {
              "name": "2+1 years",
              "loan_roi": 22.1
            },
            "48": {
              "name": "3+1 years",
              "loan_roi":  20.0
            }
}
										
d_l1 =  {
            "12": {
              "name": "1 year",
              "loan_roi": 26.0
            },
            "24": {
              "name": "1+ 1 year",
              "loan_roi": 25.7
            },
            "36": {
              "name": "2+1 years",
              "loan_roi": 23.8
            },
            "48": {
              "name": "3+1 years",
              "loan_roi": 21.9
            }
}
								
d_l2 =  {
            "12": {
              "name": "1 year",
              "loan_roi": 27.0
            },
            "24": {
              "name": "1+ 1 year",
              "loan_roi": 26.0
            },
            "36": {
              "name": "2+1 years",
              "loan_roi": 24.1
            },
            "48": {
              "name": "3+1 years",
              "loan_roi": 22.3

            }
}
							
d_l3 = {
            "12": {
              "name": "1 year",
              "loan_roi": 27.2
            },
            "24": {
              "name": "1+ 1 year",
              "loan_roi": 26.4
            },
            "36": {
              "name": "2+1 years",
              "loan_roi": 24.8
            },
            "48": {
              "name": "3+1 years",
              "loan_roi": 23.0


            }
}
			
e_l0 =  {
            "12": {
              "name": "1 year",
              "loan_roi": 25.3
            },
            "24": {
              "name": "1+ 1 year",
              "loan_roi": 24.4
            },
            "36": {
              "name": "2+1 years",
              "loan_roi": 22.6
            },
            "48": {
              "name": "3+1 years",
              "loan_roi":  20.5
            }
}
												
e_l1 =  {
            "12": {
              "name": "1 year",
              "loan_roi": 26.5
            },
            "24": {
              "name": "1+ 1 year",
              "loan_roi": 26.2
            },
            "36": {
              "name": "2+1 years",
              "loan_roi": 24.3
            },
            "48": {
              "name": "3+1 years",
              "loan_roi": 22.4
            }
}

e_l2 =  {
            "12": {
              "name": "1 year",
              "loan_roi": 27.5
            },
            "24": {
              "name": "1+ 1 year",
              "loan_roi": 26.5
            },
            "36": {
              "name": "2+1 years",
              "loan_roi": 24.6
            },
            "48": {
              "name": "3+1 years",
              "loan_roi": 22.8

            }
}
									
e_l3 = {
            "12": {
              "name": "1 year",
              "loan_roi": 27.7
            },
            "24": {
              "name": "1+ 1 year",
              "loan_roi": 26.9
            },
            "36": {
              "name": "2+1 years",
              "loan_roi": 25.3
            },
            "48": {
              "name": "3+1 years",
              "loan_roi": 23.5	
            }
}


# class OutletQuoteCategory(TimeStampedModel):
#     uuid = models.UUIDField(default=uuid.uuid4, unique=True)
#     name = models.CharField(max_length=50, null=True, blank=True, unique=True)
#     l0 = JSONField(null=True)
#     l1 = JSONField(null=True)
#     l2 = JSONField(null=True)
#     l3 = JSONField(null=True)
#     is_active = models.BooleanField(default=True)

#     class Meta:
#         db_table = 'outlet_quote_category'

